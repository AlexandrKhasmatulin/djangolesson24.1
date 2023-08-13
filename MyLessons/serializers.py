from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from MyLessons.lessons.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    number_of_lessons = SerializerMethodField()
    def get_number_of_lessons(self, course):
        return Course.objects.filter(lesson=course.lesson).count()


    class Meta:
        model = Course
        fields = '__all__'
