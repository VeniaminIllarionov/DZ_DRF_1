from material.apps import CoursesConfig
from rest_framework.routers import DefaultRouter
from django.urls import path
from material.views import (CourseViewSet, LessonList, LessonCreate, LessonRetrieve, LessonUpdate, LessonDelete,
                            SubscriptionCreateAPIView)

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonList.as_view(), name='lesson_list'),
    path('lesson/create', LessonCreate.as_view(), name='lesson_create'),
    path('lesson/<int:pk>', LessonRetrieve.as_view(), name='lesson_get'),
    path('lesson/update/<int:pk>', LessonUpdate.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>', LessonDelete.as_view(), name='lesson_delete'),
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
]
urlpatterns += router.urls
