from django.urls import path, include
from .views import *
app_name="users"
urlpatterns=[
    path("profile/", ProfileDetailView.as_view(),name="profile"),
    path("login/", CustomLoginView.as_view(),name="login"),
    path("logout/", CustomLogoutView.as_view(),name="logout"),
    path("register/", RegisterView.as_view(),name="register"),
]
