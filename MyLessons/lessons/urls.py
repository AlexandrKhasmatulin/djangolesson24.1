from django.urls import path


from rest_framework.routers import DefaultRouter

from MyLessons.lessons.apps import LessonsConfig
from MyLessons.lessons.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = LessonsConfig.name
router = DefaultRouter()
router.register(r'lessons',CourseViewSet, basename='lessons')
urlpatterns = [
                path('lesson/create', LessonCreateAPIView.as_view(), name='lesson-create'),
                path('lesson/list', LessonListAPIView.as_view(), name='lesson-list'),
                path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
                path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-destroy'),
]+router.urls