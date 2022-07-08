from django.shortcuts import render, get_object_or_404, redirect
from .models import GuestDetails
from bookings.models import BookingDetails, HotelDetails


def Home(request):
    if 'username' in request.session:
        return render(request, 'Home.html', {'name': request.session['username']})
    return render(request, 'Home.html')

def login(request):
    if 'username' in request.session:
        return redirect('Home')
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        if '@' in str(user_name):
            record = get_object_or_404(GuestDetails, email=user_name)
        else:
            record = get_object_or_404(GuestDetails, user_name=user_name)
        if password == record.password:
            request.session['username'] = record.first_name+" "+record.last_name
            request.session['user_id'] = record.user_name
            return redirect('Home')
        else:
            return render(request, 'login.html', {'message': 'User id or password is incorrect'})
    return render(request, 'login.html')

def signup(request):
    if 'username' in request.session:
        return redirect('Home')
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address1') + "," + request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        adhaar_no = request.POST.get('adhaar_no')

        try:
            record = GuestDetails.objects.get(email=str(email))
            return render(request, 'signup.html', {'message': 'Email already exists. Please login to continue'})
        except GuestDetails.DoesNotExist:
            new_user = GuestDetails(user_name=user_name, email=email, first_name=first_name, last_name=last_name,
                                    password=password, phone_number=phone_number, address=address, state=state,
                                    city=city, country=country, adhaar_no=adhaar_no)
            new_user.save()
            return redirect('Home')
    return render(request, 'signup.html')

def logout(request):
    if 'username' in request.session:
        del request.session['username']
        return redirect('Home')

def dashboard(request):
    if 'username' in request.session:
        bookings = BookingDetails.objects.filter(guest_id=request.session['user_id']).filter(booking_status='B')
        details = []
        for booking in bookings:
            details.append((booking, HotelDetails.objects.get(pk=booking.hotel_id).name))
        return render(request, 'dashboard.html', {'name': request.session['username'],
                                                  'details': details})
    else:
        return redirect('Home')

def profile(request):
    if 'username' in request.session:
        record = get_object_or_404(GuestDetails, user_name=request.session['user_id'])
        return render(request, 'profile.html', {'name': request.session['username'], 'record': record})
    else:
        return redirect('Home')

def booking_history(request):
    if 'username' in request.session:
        confirmed_bookings = BookingDetails.objects.filter(guest_id=request.session['user_id']).filter(
            booking_status='B')
        cancelled_bookings = BookingDetails.objects.filter(guest_id=request.session['user_id']).filter(
            booking_status='C1')
        confirmed_details, cancelled_details = [], []
        for confirmed_booking in confirmed_bookings:
            confirmed_details.append((confirmed_booking, HotelDetails.objects.get(pk=confirmed_booking.hotel_id).name))
        for cancelled_booking in cancelled_bookings:
            cancelled_details.append((cancelled_booking, HotelDetails.objects.get(pk=cancelled_booking.hotel_id).name))
        return render(request, 'booking_history.html', {'name': request.session['username'],
                                                        'confirmed_details': confirmed_details,
                                                        'cancelled_details': cancelled_details})
    else:
        return redirect('Home')

