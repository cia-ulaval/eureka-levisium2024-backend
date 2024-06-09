from flask import Flask
from flask_cors import CORS
from ScoringResource import ScoringResource
from MapResource import MapResource
from MapService import MapService
from ScoringService import ScoringService
from Map import Map
from Mission import Mission
import os

app = Flask(__name__)
map: Map = Map()
mission: Mission = Mission()
map_service: MapService = MapService(map, mission)
scoring_service: ScoringService = ScoringService(map, mission)

# Create the API
ScoringResource(app, scoring_service)
MapResource(app, map_service)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:8081"}})
print('SERVER STARTED')


