from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from material.models import Course, Lesson, Subscription
from material.paginators import MaterialPagination
from material.permissions import IsModerator, IsOwner
from material.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from material.tasks import send_email_task


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet for Course"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MaterialPagination

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModerator,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (IsOwner | ~IsModerator,)
        return super().get_permissions()

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        course_id = instance.id
        send_email_task(course_id)
        return instance





class LessonCreate(generics.CreateAPIView):
    """Lesson create endpoint"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator, ]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonList(generics.ListAPIView):
    """Lesson list endpoint"""
    queryset = Lesson.objects.all()
    pagination_class = MaterialPagination
    serializer_class = LessonSerializer
    permission_classes = [IsModerator | IsOwner, ]


class LessonRetrieve(generics.RetrieveAPIView):
    """Lesson one output endpoint"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModerator | IsOwner, ]


class LessonUpdate(generics.UpdateAPIView):
    """Lesson update endpoint"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModerator | IsOwner, ]

    def perform_update(self, serializer):
        update_lesson = serializer.save()
        update_lesson.owner = self.request.user
        update_lesson.save()



class LessonDelete(generics.DestroyAPIView):
    """Lesson delete endpoint"""
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, ~IsModerator]


class SubscriptionCreateAPIView(APIView):
    """Subscription create or delete endpoint"""
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course = generics.get_object_or_404(Course, pk=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course)
        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка удалена'
            send_email_task(course_id)
        else:
            Subscription.objects.create(user=user, course=course)
            message = 'Подписка добавлена'
            send_email_task(course_id)
        return Response({"message": message})
