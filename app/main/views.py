from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from datetime import datetime as dt
from ..models import User

from .. import db,photos
from . import main

@main.route('/')
def index():
  '''function that renders the homepage'''
  title = 'Challenge yourself with one of a kind pitch deck '
 
  return render_template('index.html', title=title)