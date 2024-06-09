# user_panel/urls.py
from django.contrib.auth.views import PasswordChangeView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('aviation_news/', views.aviation_news, name='aviation_news'),
    path('profile/', views.user_profile, name='user_profile'),
    path('flights/', views.flight_information, name='flight_information'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
]
