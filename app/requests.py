
from .models import Playlist
import urllib.request
import requests
import json
from .models import Playlist

secret_key = None
api_key = None
base_url = None


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
    print(image_data['coverart'])

    if data: 
      playlist_obj = Playlist(id=id,url=url,subtitle=subtitle,title=title,image=image)
      playlist_results.append(playlist_obj)
      print(playlist_results)
  return playlist_results


def configure_request(app):
  '''function that configures the request object needed for running the application'''
  global secret_key
  
  secret_key = app.config['SECRET_KEY']




