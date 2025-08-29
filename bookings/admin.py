from django.contrib import admin
from .models import Destination, Package, Booking, UserProfile

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'created_at')
    list_filter = ('country', 'created_at')
    search_fields = ('name', 'city', 'country')
    ordering = ('name',)

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'package_type', 'price', 'duration_days', 'available_seats', 'departure_date')
    list_filter = ('package_type', 'destination', 'departure_date', 'includes_flight', 'includes_hotel')
    search_fields = ('name', 'destination__name', 'destination__city')
    ordering = ('departure_date',)
    date_hierarchy = 'departure_date'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'package', 'travel_date', 'number_of_travelers', 'total_price', 'status', 'booking_date')
    list_filter = ('status', 'booking_date', 'travel_date', 'package__destination')
    search_fields = ('user__username', 'user__email', 'package__name')
    ordering = ('-booking_date',)
    date_hierarchy = 'booking_date'
    readonly_fields = ('booking_date',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'date_of_birth', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'user__email', 'phone_number')
    ordering = ('user__username',)
