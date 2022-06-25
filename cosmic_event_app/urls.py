from django.urls import path
from . import views

app_name = 'cosmic_event_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_event, name='create'),
    path('map/', views.map, name='map'),
    path('event_retrieve', views.event_retrieve, name='event_retrieve'),
    path('event_detail/<int:pk>', views.event_detail, name='event_detail'),



]
