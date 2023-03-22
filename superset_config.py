import os

#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
ROW_LIMIT = 5000
SUPERSET_WEBSERVER_PORT = 8080
SECRET_KEY = os.environ.get('SECRET_KEY')
WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = True
MAPBOX_API_KEY = os.environ.get('MAPBOX_API_KEY')
