# Get Popular Times API


## Table Of Contents
1. [Introduction](#introduction)
2. [Usage](#usage)
3. [Further Development](#further-development)

### Introduction
This is a Flask based app which serves as an API to allow users to poll Google for the Popular Times of bars and clubs.
The API returns the Popular Times as a percentage of the most popular time for that particular day.

### Usage
To use this API, first you will need to run `app.py`. Once the Flask app is up an running you can navigate to 
`/api/v1/poptimes?bar=[VENUE_NAME]&city=[LOCATION]`. This will return a list of the Popular Times for that specific venue in JSON format.


### Further Development
TBD
