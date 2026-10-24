from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Announcement, Reaction, Comment

ALLOWED_REACTIONS = {'heart', 'thumbs_up', 'thumbs_down'}


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # скільки реакцій кожного типу
        counts = (
            Reaction.objects.filter(announcement=self.object)
            .values('reaction_type')
            .annotate(total=Count('id'))
        )
        context['reaction_counts'] = {c['reaction_type']: c['total'] for c in counts}

        # яку реакцію обрав поточний користувач
        context['user_reaction'] = None
        if self.request.user.is_authenticated:
            reaction = Reaction.objects.filter(
                announcement=self.object, user=self.request.user
            ).first()
            if reaction:
                context['user_reaction'] = reaction.reaction_type

        return context


@login_required
def add_reaction(request, pk, reaction_type):
    announcement = get_object_or_404(Announcement, pk=pk)

    if reaction_type in ALLOWED_REACTIONS:
        existing_reaction = Reaction.objects.filter(
            announcement=announcement, user=request.user
        ).first()

        if existing_reaction:
            if existing_reaction.reaction_type == reaction_type:
                existing_reaction.delete()  # повторний клік скасовує реакцію
            else:
                existing_reaction.reaction_type = reaction_type
                existing_reaction.save()  # зміна типу реакції
        else:
            Reaction.objects.create(
                announcement=announcement,
                user=request.user,
                reaction_type=reaction_type
            )

    return redirect(reverse('announcement_detail', args=[pk]) + '#reactions')


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