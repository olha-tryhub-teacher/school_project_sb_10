from django.contrib import admin

from .models import Poll, Question, Choice, PollResponse, Answer

admin.site.register(Poll)
