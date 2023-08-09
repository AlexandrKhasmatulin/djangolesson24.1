from django.db import models
NULLABLE = {'blank': True, 'null': True}
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.TextField(max_length=500, verbose_name='Описание курса')
    preview = models.ImageField(upload_to='users/', verbose_name='превью', **NULLABLE)
    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(max_length=500, verbose_name='Описание урока')
    preview = models.ImageField(upload_to='users/', verbose_name='превью', **NULLABLE)
    linkvideo = models.URLField(verbose_name='превью', **NULLABLE)
    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Урок '
        verbose_name_plural = 'Уроки'