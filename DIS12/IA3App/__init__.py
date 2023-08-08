from flask import Flask
from config import Config
from flask_wtf.csrf import CSRFProtect
from flask_mongoengine import MongoEngine
from flask_restx import Api
csrf = CSRFProtect()



app = Flask(__name__)
csrf.init_app(app)
app.config.from_object(Config)


from DIS12.IA3App import routes

# cloudflared tunnel --url http://127.0.0.1:5000

# {% for data in courseData %}
#         <tr>
#             <td scope = 'row'>{{ data["course_id"] }}</td>
#             <td>{{ data["title"] }}</td>
#             <td>{{ data["description"] }}</td>
#             <td>{{ data["credits"] }}</td>
#             <td>{{ data["term"] }}</td>
#             <td>
