from django.db import models
from groups.models import Group

class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.group.name} - {self.date}"