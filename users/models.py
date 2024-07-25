from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings
from materials.models import Course, Lesson
from services import NULLABLE


class User(AbstractUser):
    role = models.CharField(max_length=15, verbose_name='роль')
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    city = models.CharField(max_length=150, verbose_name='Город', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'

