from django.db import models
from users.models import User
from schedule.models import Lesson

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.name} - {self.lesson}"