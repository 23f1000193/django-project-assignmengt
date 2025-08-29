from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from bookings.models import Destination, Package
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate the database with sample destinations and packages'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create sample destinations
        destinations_data = [
            {
                'name': 'Paris Adventure',
                'description': 'Experience the magic of Paris with its iconic Eiffel Tower, world-class museums, and charming cafes. Discover the City of Light through guided tours, Seine River cruises, and authentic French cuisine.',
                'country': 'France',
                'city': 'Paris'
            },
            {
                'name': 'Tokyo Explorer',
                'description': 'Immerse yourself in the vibrant culture of Tokyo, from traditional temples to cutting-edge technology. Experience the perfect blend of ancient traditions and modern innovation.',
                'country': 'Japan',
                'city': 'Tokyo'
            },
            {
                'name': 'New York City Experience',
                'description': 'Discover the Big Apple with its iconic landmarks, Broadway shows, and diverse neighborhoods. From Times Square to Central Park, experience the energy of NYC.',
                'country': 'USA',
                'city': 'New York'
            },
            {
                'name': 'Bali Paradise',
                'description': 'Escape to the tropical paradise of Bali with its stunning beaches, lush rice terraces, and spiritual temples. Experience the perfect blend of relaxation and adventure.',
                'country': 'Indonesia',
                'city': 'Bali'
            },
            {
                'name': 'London Discovery',
                'description': 'Explore the historic city of London with its royal palaces, world-famous museums, and iconic landmarks. Experience British culture and history at its finest.',
                'country': 'UK',
                'city': 'London'
            },
            {
                'name': 'Sydney Adventure',
                'description': 'Discover the beautiful harbor city of Sydney with its iconic Opera House, stunning beaches, and vibrant culture. Experience the best of Australian lifestyle.',
                'country': 'Australia',
                'city': 'Sydney'
            }
        ]
        
        destinations = []
        for dest_data in destinations_data:
            destination, created = Destination.objects.get_or_create(
                name=dest_data['name'],
                defaults=dest_data
            )
            destinations.append(destination)
            if created:
                self.stdout.write(f'Created destination: {destination.name}')
        
        # Create sample packages
        packages_data = [
            {
                'destination': destinations[0],  # Paris
                'name': 'Paris Essential Tour',
                'description': 'A comprehensive 5-day tour of Paris including Eiffel Tower, Louvre Museum, Notre-Dame Cathedral, and Seine River cruise.',
                'package_type': 'basic',
                'duration_days': 5,
                'price': 899.99,
                'available_seats': 20,
                'departure_date': date.today() + timedelta(days=30),
                'return_date': date.today() + timedelta(days=35),
                'includes_flight': True,
                'includes_hotel': True,
                'includes_meals': False,
                'includes_transport': True
            },
            {
                'destination': destinations[0],  # Paris
                'name': 'Paris Luxury Experience',
                'description': 'A premium 7-day luxury tour of Paris with 5-star accommodations, gourmet dining, and exclusive experiences.',
                'package_type': 'luxury',
                'duration_days': 7,
                'price': 2499.99,
                'available_seats': 10,
                'departure_date': date.today() + timedelta(days=45),
                'return_date': date.today() + timedelta(days=52),
                'includes_flight': True,
                'includes_hotel': True,
                'includes_meals': True,
                'includes_transport': True
            },
            {
                'destination': destinations[1],  # Tokyo
                'name': 'Tokyo Cultural Journey',
                'description': 'Explore the rich culture of Tokyo with visits to ancient temples, traditional gardens, and modern districts.',
                'package_type': 'premium',
                'duration_days': 6,
                'price': 1299.99,
                'available_seats': 15,
                'departure_date': date.today() + timedelta(days=60),
                'return_date': date.today() + timedelta(days=66),
                'includes_flight': True,
                'includes_hotel': True,
                'includes_meals': True,
                'includes_transport': True
            },
            {
                'destination': destinations[2],  # New York
                'name': 'NYC City Break',
                'description': 'A perfect 4-day city break in New York with visits to major attractions and Broadway show.',
                'package_type': 'basic',
                'duration_days': 4,
                'price': 799.99,
                'available_seats': 25,
                'departure_date': date.today() + timedelta(days=20),
                'return_date': date.today() + timedelta(days=24),
                'includes_flight': True,
                'includes_hotel': True,
                'includes_meals': False,
                'includes_transport': True
            },
            {
                'destination': destinations[3],  # Bali
                'name': 'Bali Beach Retreat',
                'description': 'Relax in the tropical paradise of Bali with beachfront accommodation and spa treatments.',
                'package_type': 'premium',
                'duration_days': 8,
                'price': 1599.99,
                'available_seats': 12,
                'departure_date': date.today() + timedelta(days=75),
                'return_date': date.today() + timedelta(days=83),
                'includes_flight': True,
                'includes_hotel': True,
                'includes_meals': True,
                'includes_transport': True
            },
            {
                'destination': destinations[4],  # London
                'name': 'London Royal Tour',
                'description': 'Experience the royal side of London with visits to Buckingham Palace, Tower of London, and Windsor Castle.',
                'package_type': 'premium',
                'duration_days': 5,
                'price': 1199.99,
                'available_seats': 18,
                'departure_date': date.today() + timedelta(days=40),
                'return_date': date.today() + timedelta(days=45),
                'includes_flight': True,
                'includes_hotel': True,
                'includes_meals': False,
                'includes_transport': True
            },
            {
                'destination': destinations[5],  # Sydney
                'name': 'Sydney Coastal Adventure',
                'description': 'Explore Sydney\'s stunning coastline with harbor cruises, beach visits, and coastal walks.',
                'package_type': 'basic',
                'duration_days': 6,
                'price': 1399.99,
                'available_seats': 16,
                'departure_date': date.today() + timedelta(days=90),
                'return_date': date.today() + timedelta(days=96),
                'includes_flight': True,
                'includes_hotel': True,
                'includes_meals': False,
                'includes_transport': True
            }
        ]
        
        for package_data in packages_data:
            package, created = Package.objects.get_or_create(
                name=package_data['name'],
                destination=package_data['destination'],
                defaults=package_data
            )
            if created:
                self.stdout.write(f'Created package: {package.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
