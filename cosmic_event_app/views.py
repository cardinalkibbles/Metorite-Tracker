from django.shortcuts import render, redirect
from django.urls import reverse
from .models import CustomUser, CosmicEvent


# Create your views here.


def index(request):
    return render(request, 'cosmic_event/index.html')


def create_event(request):
    if request.method == 'GET':
        return render(request, 'cosmic_event/create_event.html')
    elif request.method == 'POST':
        form = request.POST
        name = form.get('name')
        mass = form.get('mass')
        found = form.get('found')
        date = form.get('date')
        latitude = form.get('latitude')
        longitude = form.get('longitude')
        user = request.user
        meteorite = CosmicEvent.objects.create(
            name=name, mass=mass, found=found, date=date,
            latitude=latitude, longitude=longitude, user=user)
        return redirect(reverse('users_app:profile'))
