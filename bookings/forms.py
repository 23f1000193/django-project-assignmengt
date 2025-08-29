from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, UserProfile, Package
from django.core.exceptions import ValidationError
from datetime import date

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'address', 'date_of_birth', 'passport_number')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class BookingForm(forms.ModelForm):
    travel_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Select your preferred travel date"
    )
    
    class Meta:
        model = Booking
        fields = ('travel_date', 'number_of_travelers', 'special_requests', 'contact_phone', 'contact_email')
        widgets = {
            'special_requests': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        self.package = kwargs.pop('package', None)
        super().__init__(*args, **kwargs)
        if self.package:
            self.fields['travel_date'].help_text = f"Select a date between {self.package.departure_date} and {self.package.return_date}"
    
    def clean_travel_date(self):
        travel_date = self.cleaned_data.get('travel_date')
        if self.package:
            if travel_date < self.package.departure_date or travel_date > self.package.return_date:
                raise ValidationError(f"Travel date must be between {self.package.departure_date} and {self.package.return_date}")
        return travel_date
    
    def clean_number_of_travelers(self):
        number_of_travelers = self.cleaned_data.get('number_of_travelers')
        if self.package and number_of_travelers > self.package.available_seats:
            raise ValidationError(f"Only {self.package.available_seats} seats available for this package")
        return number_of_travelers

class PackageSearchForm(forms.Form):
    destination = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': 'Search destinations...'}))
    package_type = forms.ChoiceField(choices=[('', 'All Types')] + Package.PACKAGE_TYPES, required=False)
    min_price = forms.DecimalField(required=False, min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Min Price'}))
    max_price = forms.DecimalField(required=False, min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Max Price'}))
    departure_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    duration_min = forms.IntegerField(required=False, min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Min Days'}))
    duration_max = forms.IntegerField(required=False, min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Max Days'}))
