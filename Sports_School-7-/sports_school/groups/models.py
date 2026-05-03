from django.db import models
from users.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name