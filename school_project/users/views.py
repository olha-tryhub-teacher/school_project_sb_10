from django.shortcuts import render

# Create your views here.


class User(UserView):
    model = models.User
    context_object_name = "user"
    template_name = "tasks/task_list.html"
