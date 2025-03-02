from flask import Flask
from flask_cors import CORS
from controller.base_routes import set_routes

def get_app():
    server = Flask(__name__)
    CORS(server)
    set_routes(server)
    return server