# Get Popular Times API


## Table Of Contents
1. [Introduction](#introduction)
2. [Usage](#usage)
3. [Further Development](#further-development)

### Introduction
This is a Flask based app which serves as an API to allow users to poll Google for the Popular Times of bars and clubs.
The API returns the Popular Times as a percentage of the most popular time for that particular day.
V2 has been updated to first work with how Google now presents their data, and secondly, to get mor information.

### Usage
To use this API, first you will need to run `app.py`. Once the Flask app is up an running you can navigate to 
`/api/v2/poptimes?bar=[VENUE_NAME]&city=[LOCATION]` to get the popular time data, `/api/v2/ratings?bar=[VENUE_NAME]&city=[LOCATION]`
to get the rating, `/api/v2/website?bar=[VENUE_NAME]&city=[LOCATION]` to get the website url for the venue, or
`/api/v2/all?bar=[VENUE_NAME]&city=[LOCATION]` to get all this data returned together.

### Further Development
TBD
