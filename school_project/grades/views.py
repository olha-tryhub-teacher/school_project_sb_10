from django.views.generic import ListView, DetailView
from .models import Student, Teacher, Subject, Grade


class StudentListView(ListView):
    model = Student
    context_object_name = "students"
    template_name = "grades/student_list.html"
    paginate_by = 10


class StudentDetailView(DetailView):
    model = Student
    context_object_name = "student"
    template_name = "grades/student_detail.html"


class TeacherListView(ListView):
    model = Teacher
    context_object_name = "teachers"
    template_name = "grades/teacher_list.html"
    paginate_by = 10


class SubjectListView(ListView):
    model = Subject
    context_object_name = "subjects"
    template_name = "grades/subject_list.html"
    paginate_by = 10


class GradeListView(ListView):
    model = Grade
    context_object_name = "grades"
    template_name = "grades/grade_list.html"
    paginate_by = 10