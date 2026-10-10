from django.views.generic import ListView
from .models import Grade


class GradeListView(ListView):
    model = Grade
    context_object_name = "grades"
    template_name = "grades/grade_list.html"
    paginate_by = 10