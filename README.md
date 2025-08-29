# TravelEase - Travel Booking Web Application

A comprehensive travel booking web application built with Django that allows users to view available travel options, book tickets, and manage their bookings.

## Features

### For Users
- **Browse Destinations**: Explore various travel destinations with detailed information
- **Search Packages**: Filter and search travel packages by destination, price, duration, and type
- **User Registration & Authentication**: Secure user registration and login system
- **Book Travel Packages**: Easy booking process with real-time price calculation
- **Manage Bookings**: View booking history, cancel bookings, and track booking status
- **User Profile**: Update personal information and travel preferences
- **Responsive Design**: Modern, mobile-friendly interface

### For Administrators
- **Admin Dashboard**: Comprehensive admin interface for managing all data
- **Destination Management**: Add, edit, and manage travel destinations
- **Package Management**: Create and manage travel packages with detailed information
- **Booking Management**: View and manage all user bookings
- **User Management**: Monitor user accounts and profiles

## Technology Stack

- **Backend**: Django 5.2.5
- **Database**: SQLite (can be easily configured for PostgreSQL/MySQL)
- **Frontend**: Bootstrap 5.3.0, Font Awesome 6.4.0
- **Authentication**: Django's built-in authentication system
- **Admin Interface**: Django Admin

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd django-project-assignment
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Populate with sample data (optional)**
   ```bash
   python manage.py populate_sample_data
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## Project Structure

```
travel_booking/
├── manage.py
├── travel_booking/          # Main project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── bookings/               # Main application
│   ├── __init__.py
│   ├── admin.py           # Admin interface configuration
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Form classes
│   ├── urls.py            # URL patterns
│   ├── templates/         # HTML templates
│   │   └── bookings/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── package_list.html
│   │       ├── package_detail.html
│   │       ├── create_booking.html
│   │       ├── booking_detail.html
│   │       ├── user_dashboard.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── destination_list.html
│   │       └── destination_detail.html
│   └── management/        # Custom management commands
│       └── commands/
│           └── populate_sample_data.py
├── static/               # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── media/               # User-uploaded files
└── README.md
```

## Database Models

### Destination
- Name, description, country, city
- Image upload support
- Timestamps for creation and updates

### Package
- Linked to destinations
- Package types: Basic, Premium, Luxury
- Duration, price, available seats
- Departure and return dates
- Inclusion flags (flight, hotel, meals, transport)

### Booking
- User and package relationships
- Travel date, number of travelers
- Total price calculation
- Booking status (pending, confirmed, cancelled, completed)
- Contact information and special requests

### UserProfile
- Extended user information
- Phone number, address, date of birth
- Passport number for travel documentation

## Key Features Explained

### 1. Package Search & Filtering
- Search by destination name, city, or country
- Filter by package type (Basic, Premium, Luxury)
- Price range filtering
- Duration filtering
- Date-based filtering

### 2. Booking System
- Real-time seat availability checking
- Automatic price calculation based on number of travelers
- Date validation within package availability
- Booking confirmation with unique booking ID

### 3. User Dashboard
- Complete booking history
- Booking status tracking
- Profile management
- Booking cancellation (for pending bookings)

### 4. Admin Interface
- Comprehensive CRUD operations for all models
- Booking management with status updates
- User and profile management
- Package and destination management

## Usage Guide

### For Regular Users

1. **Browse Packages**: Visit the home page to see featured packages or go to "Packages" to view all available options
2. **Search & Filter**: Use the search form to find specific packages based on your preferences
3. **Register/Login**: Create an account or log in to make bookings
4. **Book a Package**: Click "Book Now" on any package to start the booking process
5. **Manage Bookings**: Access your dashboard to view all bookings and manage them

### For Administrators

1. **Access Admin**: Go to `/admin/` and log in with superuser credentials
2. **Manage Data**: Use the admin interface to add/edit destinations, packages, and manage bookings
3. **Monitor Bookings**: Track booking statuses and update them as needed
4. **User Management**: Monitor user accounts and profiles

## Sample Data

The application comes with sample data including:
- 6 popular destinations (Paris, Tokyo, New York, Bali, London, Sydney)
- 7 travel packages with varying types, durations, and prices
- Realistic departure dates and pricing

## Customization

### Adding New Destinations
1. Access the admin interface
2. Go to "Destinations" section
3. Click "Add Destination"
4. Fill in the required information

### Creating New Packages
1. Access the admin interface
2. Go to "Packages" section
3. Click "Add Package"
4. Select a destination and fill in package details

### Modifying Templates
- All templates are located in `bookings/templates/bookings/`
- The base template (`base.html`) contains the main layout and styling
- Customize CSS in the base template or create separate CSS files

## Security Features

- CSRF protection on all forms
- User authentication and authorization
- Secure password handling
- Input validation and sanitization
- Admin interface security

## Future Enhancements

- Payment gateway integration
- Email notifications for bookings
- Review and rating system
- Advanced search filters
- Multi-language support
- API endpoints for mobile apps
- Real-time chat support
- Weather integration for destinations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For support or questions, please contact the development team or create an issue in the repository.

---

**TravelEase** - Making travel booking simple and enjoyable!
