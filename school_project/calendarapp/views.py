from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import CalendarDay, CalendarEvent, Event


class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"
    ordering = ["-date_publication"]


class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"


class CalendarView(ListView):
    model = CalendarDay
    template_name = "events/calendar.html"
    context_object_name = "calendar_days"
    ordering = ["date"]


class CalendarDayDetailView(DetailView):
    model = CalendarDay
    template_name = "events/calendar_day_detail.html"
    context_object_name = "calendar_day"


def home(request):
    events = Event.objects.order_by("-date_publication")[:6]

    return render(
        request,
        "events/home.html",
        {"events": events}
    )