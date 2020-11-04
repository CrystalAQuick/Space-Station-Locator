"""
    Title: Where is the space station
    Purpose: Use webservice to find space station and plot it on a map
    Author: Crystal Quick
    Reference: https://projects.raspberrypi.org/en/projects/where-is-the-space-station
"""

import json
import urllib.request
import turtle
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']

""" Show the craft and who inside. """
for p in people:
  print(p['name'], ' in ', p['craft'])

""" Current ISS location. """
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
latitude = float(location['latitude'])
longitude = float(location['longitude'])

print('Latitude: ', latitude)
print('Longitude', longitude)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

""" Move ISS to correct location. """
iss.penup()
iss.goto(longitude, latitude)

""" Space Center, Houston. """
latitude = 29.5502
longitude = -95.097

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(longitude,latitude)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(latitude) + '&lon=' + str(longitude)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

""" Print results. """
over = result['response'][1]['risetime']
style = ('Arial', 6, 'bold')
location.write(time.ctime(over))

""" Winnipeg, Manitoba Canada. """
latitude = 49.895138
longitude = -97.138374

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(longitude,latitude)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(latitude) + '&lon=' + str(longitude)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

""" Print result. """
over = result['response'][1]['risetime']
style = ('Arial', 6, 'bold')
location.write(time.ctime(over))