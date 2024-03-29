from django.contrib.auth.models import AbstractUser
from django.db import models
NULLABLE = {'blank': True, 'null': True}
# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=100, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='фото профиля',  **NULLABLE)
    city  = models.CharField(max_length=100, verbose_name='город',  **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []