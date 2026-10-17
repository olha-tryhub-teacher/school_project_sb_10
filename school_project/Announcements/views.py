from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Announcement, Reaction, Comment


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements/announcement_list.html'
    context_object_name = 'announcements'

    def get_queryset(self):
        return Announcement.objects.filter(is_active=True).order_by('-created_at')


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcements/announcement_detail.html'
    context_object_name = 'announcement'

    def get_queryset(self):
        return Announcement.objects.filter(is_active=True)


@login_required
def add_reaction(request, pk, reaction_type):
    announcement = get_object_or_404(Announcement, pk=pk)
    existing_reaction = Reaction.objects.filter(announcement=announcement, user=request.user).first()

    if existing_reaction:
        if existing_reaction.reaction_type == reaction_type:
            existing_reaction.delete()  # Скасовуємо реакцію при повторному кліку
        else:
            existing_reaction.reaction_type = reaction_type
            existing_reaction.save()  # Змінюємо тип реакції
    else:
        Reaction.objects.create(
            announcement=announcement,
            user=request.user,
            reaction_type=reaction_type
        )

    return redirect('announcement_detail', pk=pk)


@login_required
def add_comment(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(
                announcement=announcement,
                user=request.user,
                text=text
            )
    return redirect('announcement_detail', pk=pk)