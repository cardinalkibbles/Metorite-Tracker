# Metorite-Tracker

## Goals

- Track and show the location of meteorites from the past
- Allow users to post coordinates of new meteorites
- Show location of all metorites on a map
- Custom pins for the map
- click on pin and show information (size, location, etc.)

## Models

- cosmic_events

  - mass (integer field, grams)
  - fall (boolean field, True = meteorite was found, False = meteorite is known to have fallen but never found)
  - year (integer field, year)
  - reclat (integer field, 9 characters max, decimal place of 6, latitude of meteorite)
  - reclong (integer field, 9 characters max, decimal place of 6, longitude of meteorite)
  - GeoLocation (dictionary field, uses reclong and reclat to make coordinates of meteorite)
  - User (Foreign key to CustomUser)
