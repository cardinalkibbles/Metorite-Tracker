# ![alt text](https://github.com/CardinalKibbles/Metorite-Tracker/blob/main/static/images/favicon.ico?raw=true) Metorite-Tracker ![alt text](https://github.com/CardinalKibbles/Metorite-Tracker/blob/main/static/images/favicon.ico?raw=true)

## Goals

- Track and show the location of meteorites from the past
- Allow users to post coordinates of new meteorites
- Show location of all metorites on a map
- Custom pins for the map
- click on pin and show information (size, location, etc.)
<br/>
<br/>

## Models

- cosmic_events

  - mass (decimal field, decimal place of 2 grams)
  - fall (boolean field, True = meteorite was found, False = meteorite is known to have fallen but never found)
  - year (integer field, year)  date time field possibly 
  - latitude (decimal field, 9 characters max, decimal place of 6, latitude of meteorite)
  - longitude (decimal field, 9 characters max, decimal place of 6, longitude of meteorite)
  - User (Foreign key to CustomUser)

- CustomUser
  
  - Inherit from AbstractUser 
  - default User fields

<br/>
<br/>

## User Stories
"As a user I want to be able to view all currently tracked meteorites as pins on a global map at the geographic coordinates where the meteorite landed."
<br/>
"As a user I want to be able to create an account and add new meteorites as pins at the geographic coordinates where the meteorite landed."
<br/>
"As a user I want to be able to view all the meteorites that I have added as pins on a global map at the geographic coordinates where the meteorite landed."
<br/>
"As a user I want to be able to click on a pin and view more info via a small pop-up window on the same screen."
<br/>
## Minimum viable product

My minimum viable product proposal is to have a user model able to create new pins. The user will be able to register and login to an account. The user will be able to post a pin to the map and view it on the home screen.

<br/>

## Schedule
Week 1 = users_app: models, views(register, login, profile), make pin
Week 2 = custom management command to build list view, profile list of pins and clickable link to pin
Week 3 = finish list_view interactions, push to production, create custom pins/shadow
