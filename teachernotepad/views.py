from django.urls import reverse_lazy
from .models import Student, Group, Lesson, Attendance
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
    # success_url = reverse_lazy('lesson-detail')

    def get_success_url(self):
        return reverse_lazy('group-attendance', kwargs = {'pk' : self.object.group.id, })

    def form_valid(self, form):
        # https://www.django-antipatterns.com/pattern/set-values-to-a-created-updated-object-in-a-class-based-view.html 
        group = get_object_or_404(Group, pk=self.kwargs['pk'])
        form.instance.group = group
        # for st in form.instance.group.students.all():
        #     att = Attendance(lesson=form.instance,student=st)
        #     #att.save()
        #     form.instance.attendances.add(att)
        #     print(att)
        
        return super().form_valid(form)


from django_pivot.pivot import pivot
class GroupAttendanceView(generic.DetailView):
    model = Group
    template_name = 'teachernotepad/group_attendance.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        group_attendaces = Attendance.objects.filter(lesson__group=self.object.id).order_by('student', 'lesson__datetime')
        
        context['group_attendaces'] = group_attendaces

        return context


class AttendanceUpdateView(generic.UpdateView):
    model = Attendance
    fields = ['state']
    # default is same as create view _form.html
    template_name = "teachernotepad/attendance_update.html"
    #success_url = reverse_lazy('group-attendance', kwargs = {'pk' : self.object.group.id, })

    def get_success_url(self):
        return reverse_lazy('group-attendance', kwargs = {'pk' : self.object.lesson.group.id })