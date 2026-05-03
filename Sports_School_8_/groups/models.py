from django.db import models
from users.models import User


class Group(models.Model):
    """
    Модель группы.
    Связывает тренера и участников.
    """

    name = models.CharField(max_length=100)  # название группы
    trainer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="groups"
    )

    def __str__(self):
        return self.name