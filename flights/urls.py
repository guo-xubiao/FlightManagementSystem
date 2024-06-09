# flights/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('<int:flight_id>/', views.flight_detail, name='flight_detail'),
    path('<int:flight_id>/book/', views.book_flight, name='book_flight'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

]
