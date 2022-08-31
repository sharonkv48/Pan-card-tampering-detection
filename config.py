import os
from os import  environ

class Config(object):

    Debug=False
    Testing =False

    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'pianalytix'
    UPLOADS = "/home/username/app/app/static/uploads"

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = TrueSESSION_COOKIE_SECURE = False

class DebugConfig(Config):
    DEBUG = False