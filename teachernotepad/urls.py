from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="dashboard.html"), name='dashboard'),
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/create', views.StudentCreateView.as_view(), name='student-create'),
    path('student/update/<int:pk>', views.StudentUpdateView.as_view(), name='student-update'),
    path('student/delete/<int:pk>', views.StudentDeleteView.as_view(), name='student-delete')
]
