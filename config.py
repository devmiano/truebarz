import os

class Config:
  '''class to configure url parameters'''
  URL = "https://radio-browser.p.rapidapi.com/json/stations/search"
  X_RAPIDAPI_KEY = os.environ.get('X_RAPIDAPI_KEY')
  PLAYLIST_API_BASE_URL = "https://shazam.p.rapidapi.com/songs/get-count"
  SECRET_KEY = os.environ.get('SECRET_KEY')
  PLAYLIST_API_KEY = os.environ.get('PLAYLIST_API_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  UPLOADED_PHOTOS_DEST ='app/assets/photos'
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  
class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  if SQLALCHEMY_DATABASE_URI.startswith("postgres://"): 
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)


class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://devmiano:devmiano@localhost:5432/truebarz'
  DEBUG = True
  ASSETS_DEBUG = True
  
config_options = {
  'development': DevConfig,
  'production': ProdConfig
}
  