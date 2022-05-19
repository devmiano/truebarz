import requests
import json
from .models import Radio



def configure_request(app):
  '''function that configures the request object needed for running the application'''
  global secret_key
  secret_key = app.config['SECRET_KEY']



def get_station():
  url = "https://radio-browser.p.rapidapi.com/json/stations/search"
  

  querystring = {"countrycode":"KE","reverse":"false","offset":"0","limit":"100000","hidebroken":"false"}

  headers = {
	"X-RapidAPI-Host": "radio-browser.p.rapidapi.com",
	"X-RapidAPI-Key": "45e4c3b792msha0c4aafba364711p1c32e8jsnb0149b165cd9"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)


  stations = json.loads(response.text)

  stations_by_name = []

  for station in stations:
    name = station.get('name')
    url = station.get('url')
    favicon = station.get('favicon')
    votes = station.get('votes')

    if favicon:
      obj = Radio(name=name, url=url, favicon=favicon, votes=votes)
    
      stations_by_name.append(obj)

  return stations_by_name

