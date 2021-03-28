from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    """
    Модель пользователя с добавленными полями
    и переопределенным email, требуется как уникальное,
    по нему идентифицируется пользователь
    """
    email = models.EmailField(unique=True, null=False)

    class RoleList(models.TextChoices):
        USER = 'user'
        ADMIN = 'admin'

    role = models.CharField(
        max_length=128, choices=RoleList.choices,
        default=RoleList.USER,
    )
    bio = models.TextField(default='')

    @property
    def is_admin(self):
        return (
            self.role == self.RoleList.ADMIN or self.is_superuser
        )

    def get_payload(self):
        """
        Полезная нагрузка для формирования confirmation_code
        """
        return {
            'user_id': self.id,
            'email': self.email,
            'username': self.username,
        }

    class Meta:
        ordering = ('username',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

