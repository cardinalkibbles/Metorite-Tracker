from django.core.management.base import BaseCommand
from django.utils import timezone
from cosmic_event_app.models import CosmicEvent
import json


class Command(BaseCommand):
    CosmicEvent.objects.all().delete()

    def handle(self, *args, **options):
        with open('./cosmic_event_app/management/commands/meteorites.json', encoding='utf8') as json_file:
            nasa_data = json.load(json_file)
        # nasa_data = json.dumps(nasa_data)

        for data in nasa_data:

            if data.get("year") == None or not data.get("reclat") or not data.get("reclong"):
                pass

                # found = data.get()

            else:
                date = timezone.datetime.strptime(data.get("year"), "%Y-%m-%d")
                date = timezone.make_aware(date)

                CosmicEvent.objects.create(
                    name=data.get("name", "Unknown"),
                    mass=data.get("mass", 0),
                    found=True if data.get("fall") == "Fell" else False,
                    date=date,
                    latitude=data.get("reclat"),
                    longitude=data.get("reclong"),
                )
