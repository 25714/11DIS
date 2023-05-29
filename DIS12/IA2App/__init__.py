from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_restx import Api

app = Flask(__name__)
app.config.from_object(Config)


from DIS12.IA2App import routes


# {% for data in courseData %}
#         <tr>
#             <td scope = 'row'>{{ data["course_id"] }}</td>
#             <td>{{ data["title"] }}</td>
#             <td>{{ data["description"] }}</td>
#             <td>{{ data["credits"] }}</td>
#             <td>{{ data["term"] }}</td>
#             <td>
