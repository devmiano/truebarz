from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from datetime import datetime as dt
from ..models import User
from .forms import UpdateProfile
from ..requests import get_afrobeats, get_blues, get_charts, get_dancehall, get_latin, get_playlist, get_pop, get_rock, get_station, get_world, search_music

from .. import db,photos
from . import main

@main.route('/')
def index():
  # stations = get_station()
  playlist = get_playlist()
  charts = get_charts()
  world = get_world()
  pop = get_pop()
  '''function that renders the homepage'''
  title = 'All in One Music App'
  
  

  return render_template('index.html', title=title, playlist=playlist, charts=charts, world=world, pop=pop)

@main.route('/trending')
@login_required
def trending():
  afrobeats = get_afrobeats()
  blues = get_blues()
  pop = get_pop()
  world = get_world()
  '''function that renders the homepage'''
  title = 'All in One Music App'



  return render_template('trending.html', title=title, afrobeats=afrobeats, pop=pop, blues=blues, world=world,)

@main.route('/collections')
@login_required
def collections():
  dancehall = get_dancehall()
  latin = get_latin()
  rock = get_rock()
  afrobeats = get_afrobeats()
  
  '''function that renders the homepage'''
  title = 'All in One Music App'
  
  

  return render_template('collections.html', title=title,  dancehall=dancehall, latin=latin, rock=rock, afrobeats=afrobeats)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()

  if user is None:
    abort(404)

  return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile',uname=uname))


@main.route('/search')
@login_required
def find():
  title = 'Search'
  search_music = request.args.get('query')
  if search_music:
    return redirect(url_for('main.search', query=search_music, title=title))
  
  else:
    return render_template('find.html')
  
  
  
@main.route('/search/<query>')
@login_required
def search(query):
	query_list = query.split(' ')
	query_format = "+".join(query_list)
	search_tracks = search_music(query_format)
	title = f'search results for {query}'
  
  
	return render_template('search.html',title=title, music=search_tracks)