from django.urls import path
from .views import (
    AnnouncementListView,
    AnnouncementDetailView,
    add_reaction,
    add_comment
)

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement_list'),
    path('announcement/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('announcement/<int:pk>/reaction/<str:reaction_type>/', add_reaction, name='add_reaction'),
    path('announcement/<int:pk>/comment/', add_comment, name='add_comment'),
]