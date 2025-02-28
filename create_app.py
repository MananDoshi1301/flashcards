from flask import Flask
from controller.base_routes import set_routes

def get_app():
    server = Flask(__name__)
    set_routes(server)
    return server