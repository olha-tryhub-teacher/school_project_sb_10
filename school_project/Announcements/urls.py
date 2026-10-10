from django.urls import path
from .views import AnnouncementListView, AnnouncementDetailView

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement_list'),
    path('announcement/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
]