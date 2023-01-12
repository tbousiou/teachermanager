from django.urls import reverse_lazy
from .models import Student
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