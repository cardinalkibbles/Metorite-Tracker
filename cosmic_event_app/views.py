from email import message
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from cosmic_event_app.models import CosmicEvent
from cosmic_event_app.serializers import CosmicEventSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


from .models import CustomUser, CosmicEvent


# Create your views here.


def index(request):
    return render(request, 'cosmic_event/index.html')


def map(request):
    return render(request, 'cosmic_event/map.html')


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


@api_view(['GET', 'POST'])
def event_retrieve(request):
    if request.method == 'GET':
        CosmicEvents = CosmicEvent.objects.all()
        serializer = CosmicEventSerializer(CosmicEvents, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CosmicEventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, pk):
    try:
        CosmicEvents = CosmicEvent.objects.get(pk=pk)
    except CosmicEvent.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CosmicEventSerializer(CosmicEvent)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CosmicEventSerializer(CosmicEvent, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        CosmicEvent.delete()
        return HttpResponse(status=204)
