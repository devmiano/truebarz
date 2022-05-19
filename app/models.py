from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from datetime import datetime
from . import db
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))



class User(UserMixin, db.Model):
  __tablename__ = 'users'
  
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(255))
  last_name = db.Column(db.String(255))
  username = db.Column(db.String(255), unique=True, index=True)
  email = db.Column(db.String(255), unique=True, index=True)
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String(255))
  password_hash = db.Column(db.String(255))
  playlist = db.relationship('Playlist', backref='user', lazy='dynamic')
  
  @property
  def password(self):
    raise AttributeError('you cannot read the password')
  
  @password.setter
  def password(self, password):
    self.password_hash = generate_password_hash(password)
    
  def verify_password(self, password):
    return check_password_hash(self.password_hash, password)
  
  def __repr__(self):
      return f'User {self.username}'

class Playlist(db.Model):

  __tablename__ = 'playlist'

  id = db.Column(db.Integer,primary_key=True)
  url = db.Column(db.String(255))
  subtitle = db.Column(db.String(255))
  title = db.Column(db.String(255))
  image = db.Column(db.String(255))
  users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def __repr__(self):
        return f"Playlist('{self.url}')"






    
