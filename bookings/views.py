from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Destination, Package, Booking, UserProfile
from .forms import UserRegistrationForm, UserProfileForm, BookingForm, PackageSearchForm
from decimal import Decimal

def home(request):
    """Home page with featured destinations and packages"""
    featured_destinations = Destination.objects.all()[:6]
    featured_packages = Package.objects.filter(available_seats__gt=0).order_by('departure_date')[:6]
    
    context = {
        'featured_destinations': featured_destinations,
        'featured_packages': featured_packages,
    }
    return render(request, 'bookings/home.html', context)

def package_list(request):
    """List all available packages with search and filtering"""
    packages = Package.objects.filter(available_seats__gt=0)
    search_form = PackageSearchForm(request.GET)
    
    if search_form.is_valid():
        destination = search_form.cleaned_data.get('destination')
        package_type = search_form.cleaned_data.get('package_type')
        min_price = search_form.cleaned_data.get('min_price')
        max_price = search_form.cleaned_data.get('max_price')
        departure_date = search_form.cleaned_data.get('departure_date')
        duration_min = search_form.cleaned_data.get('duration_min')
        duration_max = search_form.cleaned_data.get('duration_max')
        
        if destination:
            packages = packages.filter(
                Q(destination__name__icontains=destination) |
                Q(destination__city__icontains=destination) |
                Q(destination__country__icontains=destination)
            )
        
        if package_type:
            packages = packages.filter(package_type=package_type)
        
        if min_price:
            packages = packages.filter(price__gte=min_price)
        
        if max_price:
            packages = packages.filter(price__lte=max_price)
        
        if departure_date:
            packages = packages.filter(departure_date__gte=departure_date)
        
        if duration_min:
            packages = packages.filter(duration_days__gte=duration_min)
        
        if duration_max:
            packages = packages.filter(duration_days__lte=duration_max)
    
    # Pagination
    paginator = Paginator(packages, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_form': search_form,
        'total_packages': packages.count(),
    }
    return render(request, 'bookings/package_list.html', context)

def package_detail(request, package_id):
    """Detailed view of a specific package"""
    package = get_object_or_404(Package, id=package_id)
    related_packages = Package.objects.filter(
        destination=package.destination
    ).exclude(id=package.id)[:3]
    
    context = {
        'package': package,
        'related_packages': related_packages,
    }
    return render(request, 'bookings/package_detail.html', context)

@login_required
def create_booking(request, package_id):
    """Create a new booking for a package"""
    package = get_object_or_404(Package, id=package_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, package=package)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.package = package
            booking.total_price = package.price * booking.number_of_travelers
            
            # Update available seats
            package.available_seats -= booking.number_of_travelers
            package.save()
            
            booking.save()
            
            messages.success(request, f'Booking created successfully! Your booking ID is {booking.id}')
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = BookingForm(package=package)
    
    context = {
        'form': form,
        'package': package,
    }
    return render(request, 'bookings/create_booking.html', context)

@login_required
def booking_detail(request, booking_id):
    """View details of a specific booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    context = {
        'booking': booking,
    }
    return render(request, 'bookings/booking_detail.html', context)

@login_required
def user_dashboard(request):
    """User dashboard showing all bookings and profile"""
    user_bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    
    # Get or create user profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('user_dashboard')
    else:
        profile_form = UserProfileForm(instance=profile)
    
    context = {
        'user_bookings': user_bookings,
        'profile_form': profile_form,
        'profile': profile,
    }
    return render(request, 'bookings/user_dashboard.html', context)

@login_required
@require_POST
def cancel_booking(request, booking_id):
    """Cancel a booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if booking.status == 'pending':
        booking.status = 'cancelled'
        booking.save()
        
        # Restore available seats
        package = booking.package
        package.available_seats += booking.number_of_travelers
        package.save()
        
        messages.success(request, 'Booking cancelled successfully!')
    else:
        messages.error(request, 'This booking cannot be cancelled.')
    
    return redirect('user_dashboard')

def register(request):
    """User registration"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            
            # Log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'bookings/register.html', context)

def destination_list(request):
    """List all destinations"""
    destinations = Destination.objects.all()
    
    context = {
        'destinations': destinations,
    }
    return render(request, 'bookings/destination_list.html', context)

def destination_detail(request, destination_id):
    """Detailed view of a specific destination"""
    destination = get_object_or_404(Destination, id=destination_id)
    packages = Package.objects.filter(destination=destination, available_seats__gt=0)
    
    context = {
        'destination': destination,
        'packages': packages,
    }
    return render(request, 'bookings/destination_detail.html', context)
