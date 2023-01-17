from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Student(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk' : self.pk})


class Group(models.Model):
    title = models.CharField(max_length=60)
    subject = models.CharField(max_length=60, blank=True)

    # setting blank=true make the field optional
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'pk' : self.pk})


class Lesson(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    attendances = models.ManyToManyField(Student, through='Attendance')

    def __str__(self):
        return f"{self.group} {self.datetime}"
    
    


class Attendance(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    state = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['lesson', 'student'], name='lesson_student')
        ]

    def __str__(self):
        return f"{self.lesson} {self.student} {self.state}"