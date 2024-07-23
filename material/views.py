from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from material.models import Course, Lesson
from material.paginators import MaterialPagination
from material.permissions import IsModerator, IsOwner
from material.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
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


class LessonCreate(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator,]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonList(generics.ListAPIView):
    queryset = Lesson.objects.all()
    pagination_class = MaterialPagination
    serializer_class = LessonSerializer
    permission_classes = [IsModerator | IsOwner,]



class LessonRetrieve(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModerator | IsOwner,]


class LessonUpdate(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModerator | IsOwner,]

    def perform_update(self, serializer):
        update_lesson = serializer.save()
        update_lesson.owner = self.request.user
        update_lesson.save()


class LessonDelete(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, ~IsModerator]
