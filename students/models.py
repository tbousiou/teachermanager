from django.db import models
from django.utils import timezone
# Create your models here.


class Student(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Group(models.Model):
    title = models.CharField(max_length=60)
    subject = models.CharField(max_length=60, blank=True)

    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group} {self.datetime}"


class Attendance(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.lesson} {self.student} {self.state}"