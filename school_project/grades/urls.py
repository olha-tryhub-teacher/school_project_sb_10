from django.urls import path
from .views import (
    StudentListView,
    StudentDetailView,
    TeacherListView,
    SubjectListView,
    GradeListView,
)

app_name = "grades"

urlpatterns = [
    path("", GradeListView.as_view(), name="grade_list"),
    path("students/", StudentListView.as_view(), name="student_list"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("teachers/", TeacherListView.as_view(), name="teacher_list"),
    path("subjects/", SubjectListView.as_view(), name="subject_list"),
]