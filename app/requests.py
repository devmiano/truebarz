import urllib.request
import http.client
import requests
import json
from .models import Chart, Playlist, Radio

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


def search_music(query):
  hits_list = []
  conn = http.client.HTTPSConnection("shazam.p.rapidapi.com")
  headers = {'X-RapidAPI-Host': "shazam.p.rapidapi.com", 'X-RapidAPI-Key': "f1ecc09012msh395fade747664ecp14465djsn59429cc15c85"}
  shazam_search_url= "/search?term={}&locale=en-US&offset=0&limit=5".format(query)
  conn.request("GET", shazam_search_url, headers=headers)

  res = conn.getresponse()
  data = res.read()
  results = data.decode("utf-8")
  hits = results[0][0]
  search_hits = []
  
  for hit in hits:
    id = hit.get('id')
    url = hit.get('url')
    subtitle = hit.get('subtitle')
    title = hit.get('title')
    image_data = data.get('images')
   
    image = image_data['background']

    if hit: 
      hit_obj = Chart(id=id,url=url,subtitle=subtitle,title=title,image=image)
      search_hits.append(hit_obj)
      return search_hits


def get_charts():
  url = "https://shazam.p.rapidapi.com/charts/track"

  querystring = {"locale":"en-US","pageSize":"20","startFrom":"0"}

  headers = {
    "X-RapidAPI-Host": "shazam.p.rapidapi.com",
    "X-RapidAPI-Key": "f1ecc09012msh395fade747664ecp14465djsn59429cc15c85"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  results= json.loads(response.text)
  datas = results["tracks"]

  chart_results = []
  for data in datas:
    id = data.get('key')
    url = data.get('url')
    subtitle = data.get('subtitle')
    title = data.get('title')
    image_data = data.get('images')
   
    image = image_data['background']

    if data: 
      playlist_obj = Chart(id=id,url=url,subtitle=subtitle,title=title,image=image)
      chart_results.append(playlist_obj)
  return chart_results


def get_dancehall():
  url = "https://shazam.p.rapidapi.com/charts/track"

  querystring = {"locale":"en-US","listId":"genre-global-chart-13","pageSize":"20","startFrom":"0"}

  headers = {
    "X-RapidAPI-Host": "shazam.p.rapidapi.com",
    "X-RapidAPI-Key": "f1ecc09012msh395fade747664ecp14465djsn59429cc15c85"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  results= json.loads(response.text)
  datas = results["tracks"]

  dancehall_results = []
  for data in datas:
    id = data.get('key')
    url = data.get('url')
    subtitle = data.get('subtitle')
    title = data.get('title')
    image_data = data.get('images')
   
    image = image_data['background']

    if data: 
      playlist_obj = Chart(id=id,url=url,subtitle=subtitle,title=title,image=image)
      dancehall_results.append(playlist_obj)
  return dancehall_results

def get_world():
  url = "https://shazam.p.rapidapi.com/charts/track"

  querystring = {"locale":"en-US","listId":"genre-global-chart-12","pageSize":"20","startFrom":"0"}

  headers = {
    "X-RapidAPI-Host": "shazam.p.rapidapi.com",
    "X-RapidAPI-Key": "f1ecc09012msh395fade747664ecp14465djsn59429cc15c85"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  results= json.loads(response.text)
  datas = results["tracks"]

  world_results = []
  for data in datas:
    id = data.get('key')
    url = data.get('url')
    subtitle = data.get('subtitle')
    title = data.get('title')
    image_data = data.get('images')
   
    image = image_data['background']

    if data: 
      playlist_obj = Chart(id=id,url=url,subtitle=subtitle,title=title,image=image)
      world_results.append(playlist_obj)
  return world_results


def get_afrobeats():
  url = "https://shazam.p.rapidapi.com/charts/track"

  querystring = {"locale":"en-US","listId":"genre-global-chart-11","pageSize":"20","startFrom":"0"}

  headers = {
    "X-RapidAPI-Host": "shazam.p.rapidapi.com",
    "X-RapidAPI-Key": "f1ecc09012msh395fade747664ecp14465djsn59429cc15c85"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  results= json.loads(response.text)
  datas = results["tracks"]

  world_results = []
  for data in datas:
    id = data.get('key')
    url = data.get('url')
    subtitle = data.get('subtitle')
    title = data.get('title')
    image_data = data.get('images')
   
    image = image_data['background']

    if data: 
      playlist_obj = Chart(id=id,url=url,subtitle=subtitle,title=title,image=image)
      world_results.append(playlist_obj)
  return world_results


def get_latin():
  url = "https://shazam.p.rapidapi.com/charts/track"

  querystring = {"locale":"en-US","listId":"genre-global-chart-8","pageSize":"20","startFrom":"0"}

  headers = {
    "X-RapidAPI-Host": "shazam.p.rapidapi.com",
    "X-RapidAPI-Key": "f1ecc09012msh395fade747664ecp14465djsn59429cc15c85"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  results= json.loads(response.text)
  datas = results["tracks"]

  world_results = []
  for data in datas:
    id = data.get('key')
    url = data.get('url')
    subtitle = data.get('subtitle')
    title = data.get('title')
    image_data = data.get('images')
   
    image = image_data['background']

    if data: 
      playlist_obj = Chart(id=id,url=url,subtitle=subtitle,title=title,image=image)
      world_results.append(playlist_obj)
  return world_results


def get_rock():
  url = "https://shazam.p.rapidapi.com/charts/track"

  querystring = {"locale":"en-US","listId":"genre-global-chart-7","pageSize":"20","startFrom":"0"}

  headers = {
    "X-RapidAPI-Host": "shazam.p.rapidapi.com",
    "X-RapidAPI-Key": "f1ecc09012msh395fade747664ecp14465djsn59429cc15c85"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  results= json.loads(response.text)
  datas = results["tracks"]

  world_results = []
  for data in datas:
    id = data.get('key')
    url = data.get('url')
    subtitle = data.get('subtitle')
    title = data.get('title')
    image_data = data.get('images')
   
    image = image_data['background']

    if data: 
      playlist_obj = Chart(id=id,url=url,subtitle=subtitle,title=title,image=image)
      world_results.append(playlist_obj)
  return world_results


def get_blues():
  url = "https://shazam.p.rapidapi.com/charts/track"

  querystring = {"locale":"en-US","listId":"genre-global-chart-5","pageSize":"20","startFrom":"0"}

  headers = {
    "X-RapidAPI-Host": "shazam.p.rapidapi.com",
    "X-RapidAPI-Key": "f1ecc09012msh395fade747664ecp14465djsn59429cc15c85"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  results= json.loads(response.text)
  datas = results["tracks"]

  world_results = []
  for data in datas:
    id = data.get('key')
    url = data.get('url')
    subtitle = data.get('subtitle')
    title = data.get('title')
    image_data = data.get('images')
   
    image = image_data['background']

    if data: 
      playlist_obj = Chart(id=id,url=url,subtitle=subtitle,title=title,image=image)
      world_results.append(playlist_obj)
  return world_results


def get_pop():
  url = "https://shazam.p.rapidapi.com/charts/track"
  
  test = 1

  querystring = {"locale":"en-US","listId":"genre-global-chart-1","pageSize":"20","startFrom":"0"}

  headers = {
    "X-RapidAPI-Host": "shazam.p.rapidapi.com",
    "X-RapidAPI-Key": "f1ecc09012msh395fade747664ecp14465djsn59429cc15c85"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  results= json.loads(response.text)
  datas = results["tracks"]

  world_results = []
  for data in datas:
    id = data.get('key')
    url = data.get('url')
    subtitle = data.get('subtitle')
    title = data.get('title')
    image_data = data.get('images')
   
    image = image_data['background']

    if data: 
      playlist_obj = Chart(id=id,url=url,subtitle=subtitle,title=title,image=image)
      world_results.append(playlist_obj)
  return world_results
