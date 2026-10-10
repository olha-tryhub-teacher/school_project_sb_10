from django.shortcuts import render

from school_project_sb_10.school_project.events.models import Event

# Create your views here.
class TaskListView(Event):
    model = models.events
    template_name = 'task_list.html'
    context_object_name = 'task_list'