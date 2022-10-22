from flask import Flask
from config import Config
# from flask_restx import Api
#
# api = Api()
app = Flask(__name__)
app.config.from_object(Config)

# api.init_app(app)

from LucasNguyenFIA2DIGI import routes
