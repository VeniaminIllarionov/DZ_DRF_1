from rest_framework import viewsets

from material.models import Course, Lesson
from material.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()



