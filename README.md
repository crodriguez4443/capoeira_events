# Capoeira Events

## PROJECT GOALS
Search for Capoeira events in your area. The app will prompt you for you location and place a pin down on your location. You can also create events and add event details. Event locations are automatically uploaded to the leaflet map on the home page.

## Table of contents
- [Features](#features)
- [Homepage](#home-page)
- [CreateEvent](#create-event)
- [EventDetails](#event-details)
- [Requirements](#requirements)
- [AdditionalFeatures](#additional-potential-functionality)
- [Contact](#contact)

## Features

### Home page
- Search for events by using the interactive leaflet map on the home page
- Create events with the "Create event" button on the top right.
- See your location with a pin on the map
- See all event locations with pins on the map
- Scroll down to see a list of all events with quick event info
- Bootstrap CSS styling
### Create event
- Several user input fields (text box, single lines, date, dropdown, and address location)
- Lat/long values are created from the address information provided
- These values are displayed on the home page and allow the program to display the event on the home page map.
- Save will save the event to the project database (sqlite)
### Event details
- Click on pages to get event details.
- On details page, click "edit event" to make changes
- edit pages contain the current event info so you know what you're chainging. 

## Requirements
- Python 3.x
- Django
- See requirements.txt file

## Additional Potential Functionality
- email notifications that you event was created
- filter on home page to view events only in a designated area by address and distance or by date
- Error messages for addresses that are not able to generate lat/longs
- User authentication. Only signed in users can create events. 
- use of REST API framework to gather lat/long info instead of my jenky method
- Hosting

## Contact
- crodriguez4443@gmail.com
