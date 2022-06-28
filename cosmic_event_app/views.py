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
def event_retrieve(request, format=None):
    if request.method == 'GET':
        cosmic_events = CosmicEvent.objects.all()
        serializer = CosmicEventSerializer(cosmic_events, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CosmicEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, pk, format=None):
    try:
        cosmic_event = CosmicEvent.objects.get(pk=pk)
    except CosmicEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": f"Could not find the cosmic event object with object id of {pk}"})

    if request.method == 'GET':
        serializer = CosmicEventSerializer(cosmic_event)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CosmicEventSerializer(cosmic_event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cosmic_event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
