from django.urls import path
from . import views

app_name = 'cosmic_event_app'
urlpatterns = [
    path('', views.index, name='index'),
]


# request.userisauthenticated