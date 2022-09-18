from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'cosmic_event_app'
urlpatterns = [
    path('event_detail/<int:pk>/', views.event_detail, name='event_detail'),
    path('', views.index, name='index'),
    path('create/', views.create_event, name='create'),
    path('map/', views.map, name='map'),
    path('event_retrieve/', views.event_retrieve, name='event_retrieve'),
]

urlpatterns = format_suffix_patterns(urlpatterns)