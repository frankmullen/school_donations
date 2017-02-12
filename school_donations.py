from flask import Flask
from flask import render_template
from flask import send_from_directory
from pymongo import MongoClient
import json
import os

app = Flask(__name__)

DBS_NAME = os.environ.get('DBS_NAME')
MONGO_URI = os.environ.get('MONGO_URI')
MONGODB_HOST = os.environ.get('MONGODB_HOST')
MONGODB_PORT = os.environ.get('MONGODB_PORT')
#MONGODB_HOST = 'ds149069.mlab.com'
#MONGODB_PORT = 49069
#DBS_NAME = 'heroku_sl7272bv'
#MONGO_URI = 'mongodb://root:schoolheroku@ds149069.mlab.com:49069/heroku_sl7272bv'
COLLECTION_NAME = 'opendata_projects_clean'
FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True, 'poverty_level': True,
          'date_posted': True, 'total_donations': True, '_id': False}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donorsUS/projects")
def donor_projects():
    connection = MongoClient(MONGO_URI)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=20000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects)
    connection.close()
    return json_projects

@app.route("/donorsUS/states")
def send_geoData():
    return send_from_directory('static/data', 'us-states.JSON')

if __name__ == "__main__":
    app.run(debug=True)