from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ('manager', 'Менеджер'),
    ('client', 'Клиент'),
    ('service', 'Сервисная организация'),
)

class CustomUser(AbstractUser):
    """
    Кастомный пользователь с дополнительным полем 'role'.
    """
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        blank=True,
        null=True,
        verbose_name='Роль'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
