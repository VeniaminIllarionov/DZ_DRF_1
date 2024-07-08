from material.apps import CoursesConfig
from rest_framework.routers import DefaultRouter

from material.views import CourseViewSet

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='material')

urlpatterns = [

] + router.urls
