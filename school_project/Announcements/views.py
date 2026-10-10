from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Announcement


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements/announcement_list.html'
    context_object_name = 'announcements'

    def get_queryset(self):
        # Виводимо тільки активні оголошення, відсортовані від найновіших
        return Announcement.objects.filter(is_active=True).order_by('-created_at')


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcements/announcement_detail.html'
    context_object_name = 'announcement'

    def get_queryset(self):
        return Announcement.objects.filter(is_active=True)
