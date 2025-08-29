from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.home, name='home'),
    path('packages/', views.package_list, name='package_list'),
    path('package/<int:package_id>/', views.package_detail, name='package_detail'),
    path('package/<int:package_id>/book/', views.create_booking, name='create_booking'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('booking/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('register/', views.register, name='register'),
    path('destinations/', views.destination_list, name='destination_list'),
    path('destination/<int:destination_id>/', views.destination_detail, name='destination_detail'),
]
