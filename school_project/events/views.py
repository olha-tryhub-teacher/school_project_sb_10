from django.shortcuts import render

from school_project_sb_10.school_project.events.models import Event

from django.contrib import admin
from django.urls import include, path

# Create your views here.
class TaskListView(Event):
    model = models.events
    template_name = 'task_list.html'
    context_object_name = 'task_list'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("events.urls")),

]

from django.urls import path
from . import views

app_name = "events"


from django.urls import path
from . import views

app_name = "events"

urlpatterns = [

    path("", views.event_list, name="event_list"),


    path("create/", views.event_create, name="event_create"),

    path("<int:pk>/", views.event_detail, name="event_detail"),

    path("<int:pk>/edit/", views.event_update, name="event_update"),

    path("<int:pk>/delete/", views.event_delete, name="event_delete"),



]

