import os


class Congif(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "Secret_String"

