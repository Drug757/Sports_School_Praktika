from django.db import models


class User(models.Model):
    """
    Модель пользователя системы.
    Может быть администратором, тренером или участником.
    """

    name = models.CharField(max_length=100)  # имя пользователя
    role = models.CharField(
        max_length=50
    )  # роль: admin / trainer / participant

    def __str__(self):
        return self.name