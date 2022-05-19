import urllib.request
import requests
import json
from .models import Playlist, Radio

secret_key = None
api_key = None
base_url = None

def configure_request(app):
  '''function that configures the request object needed for running the application'''
  global secret_key
  secret_key = app.config['SECRET_KEY']

  
def get_playlist():
  url = "https://shazam.p.rapidapi.com/songs/list-recommendations"

  querystring = {"key":"484129036","locale":"en-US"}

  headers = {
    "X-RapidAPI-Host": "shazam.p.rapidapi.com",
    "X-RapidAPI-Key": "31e9cbe3d8msh574eaee9cfc96afp14b0aejsn2dbf23758e92"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  results= json.loads(response.text)
  datas = results["tracks"]

  playlist_results = []
  for data in datas:
    id = data.get('key')
    url = data.get('url')
    subtitle = data.get('subtitle')
    title = data.get('title')
    image_data = data.get('images')
   
    image = image_data['coverart']

    if data: 
      playlist_obj = Playlist(id=id,url=url,subtitle=subtitle,title=title,image=image)
      playlist_results.append(playlist_obj)
  return playlist_results


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

    if station:
      obj = Radio(name=name, url=url, favicon=favicon, votes=votes)
    
      stations_by_name.append(obj)

  return stations_by_name


