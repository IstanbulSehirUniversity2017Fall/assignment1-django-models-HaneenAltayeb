from __future__ import unicode_literals
from django.db import models


class DormStudent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_id = models.IntegerField(max_length=9)

class StudentRoom(models.Model):
    room_no = models.ForeignKey(DormStudent, on_delete=models.CASCADE)






