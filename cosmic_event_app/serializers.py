from rest_framework import serializers
from cosmic_event_app.models import CosmicEvent


class CosmicEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CosmicEvent
        fields = ['id', 'name', 'mass', 'found', 'date',
                  'latitude', 'longitude', 'user']
