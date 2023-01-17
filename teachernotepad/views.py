from django.urls import reverse_lazy
from .models import Student, Group, Lesson
from .forms import LessonForm, GroupLessonForm
from django.views import generic
# Create your views here.


class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

class StudentCreateView(generic.CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'email']


class StudentUpdateView(generic.UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'email']
    # default is same as create view _form.html
    template_name = "teachernotepad/student_update.html"

class StudentDeleteView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')


class GroupListView(generic.ListView):
    model = Group

class GroupDetailView(generic.DetailView):
    model = Group

class GroupCreateView(generic.CreateView):
    model = Group
    fields = ['title', 'subject', 'students']

class  GroupUpdateView(generic.UpdateView):
    model =  Group
    fields = ['title', 'subject', 'students']
    # default is same as create view _form.html
    template_name = "teachernotepad/group_update.html"

class GroupDeleteView(generic.DeleteView):
    model = Group
    success_url = reverse_lazy('group-list')

class LessonCreateView(generic.CreateView):
    model = Lesson
    form_class = LessonForm

    #fields = ['datetime', 'group', 'attendances']

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
class GroupLessonCreateView(generic.CreateView):
    model = Lesson
    form_class = GroupLessonForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        group = get_object_or_404(Group, pk=self.kwargs['group_pk'])
        self.object.group = group
        self.object.save()
        return super().form_valid(form)



class GroupAttendanceView(generic.DetailView):
    model = Group
    template_name = 'teachernotepad/group_attendance.html'