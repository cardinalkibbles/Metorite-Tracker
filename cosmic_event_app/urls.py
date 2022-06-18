from django.urls import path
from . import views

app_name = 'cosmic_event_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_event, name='create'),
    path('map/', views.map, name='map'),
    
]
