from django.contrib import admin
from .models import Student, Group, Lesson, Attendance
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'student', 'state']