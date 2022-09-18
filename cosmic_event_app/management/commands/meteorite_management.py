from django.core.management.base import BaseCommand
from django.utils import timezone
from cosmic_event_app.models import CosmicEvent
import json


class Command(BaseCommand):
    CosmicEvent.objects.all().delete()
    def handle(self, *args, **options):
        with open('./cosmic_event_app/management/commands/meteorites.json', encoding='utf8') as json_file:
            nasa_data = json.load(json_file) 
        
        for data in nasa_data:
            if not data.get("year") or not data.get("reclat") or not data.get("reclong"):
                pass

            else:
                date = timezone.datetime.strptime(str(data.get("year")), "%Y")
                date = timezone.make_aware(date)

                CosmicEvent.objects.create(
                    name=data.get("name", "Unknown"),
                    mass=data.get("mass", 0) or 0,
                    found=True if data.get("fall") == "Fell" else False,
                    date=date,
                    latitude=data.get("reclat"),
                    longitude=data.get("reclong"),
                )