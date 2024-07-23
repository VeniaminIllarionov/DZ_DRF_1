from rest_framework import serializers

from material.models import Course, Lesson
from material.validators import YoutubeValidation


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YoutubeValidation(field="url_video")]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'lesson_count', 'lessons', 'owner',)

