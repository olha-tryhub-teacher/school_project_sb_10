
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView

from .models import Event


class TaskListView(ListView):
    model = Event
    template_name = "task_list.html"
    context_object_name = "task_list"


def event_list(request):
    events = Event.objects.all().order_by("date")
    return render(request, "events/event_list.html", {"events": events})


@login_required
def event_create(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        date = request.POST.get("date", "").strip()
        location = request.POST.get("location", "").strip()

        if title and description and date and location:
            Event.objects.create(
                title=title,
                description=description,
                date=date,
                location=location,
                author=request.user,
            )
            messages.success(request, "Подію створено!")
            return redirect("events:event_list")

        messages.error(request, "Заповни всі поля.")

    return render(request, "events/event_form.html")


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, "events/event_detail.html", {"event": event})


@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk, author=request.user)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        date = request.POST.get("date", "").strip()
        location = request.POST.get("location", "").strip()

        if title and description and date and location:
            event.title = title
            event.description = description
            event.date = date
            event.location = location
            event.save()
            messages.success(request, "Подію оновлено!")
            return redirect("events:event_detail", pk=event.pk)

        messages.error(request, "Заповни всі поля.")

    return render(request, "events/event_form.html", {"event": event})


@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk, author=request.user)

    if request.method == "POST":
        event.delete()
        messages.success(request, "Подію видалено!")
        return redirect("events:event_list")

    return render(request, "events/event_confirm_delete.html", {"event": event})


@login_required
def event_join(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        event.participants.add(request.user)
        messages.success(request, "Ти приєднався до події!")

    return redirect("events:event_detail", pk=event.pk)


@login_required
def event_leave(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        event.participants.remove(request.user)
        messages.success(request, "Ти скасував участь у події.")

    return redirect("events:event_detail", pk=event.pk)
