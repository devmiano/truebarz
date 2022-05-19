from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from datetime import datetime as dt
from ..requests import get_station

from .. import db,photos
from . import main

@main.route('/')
def index():
  '''function that renders the homepage'''
  title = 'All in One Music App'
  stations = get_station() 
 
  return render_template('index.html', title=title, stations=stations)

