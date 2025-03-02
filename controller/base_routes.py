import os, functools
from typing import Tuple
from flask import Flask, request, jsonify
from application.write_db import DbWrite
from application.read_db import DbRead
from controller.server_utilities import *

# def verify_id(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         user_id = kwargs.get("user_id", None)
#         id = int(user_id) if user_id.isdigit() else None        
#         if not id: return error_response("Missing Required Credentials", 404)            
#         return func(*args, **kwargs)
#     return wrapper
 

def set_routes(server: Flask):

    @server.route("/", methods=["GET"])
    def hello():
        return "This is app!"

    @server.route("/cards/<user_id>", methods=["GET"])    
    def get_cards(user_id):
        id = int(user_id) if user_id.isdigit() else None        
        if not id: return error_response("Missing Required Credentials", 404)    

        filename = get_filename(id)
        cursor = DbRead(filename=filename)
        response: dict = cursor.get_cards()
        questions, result_dict = response["questions"], response["results"]
        return success_response("Data found successfully!", 200, questions=questions, results=result_dict)
    
    @server.route("/cards/<user_id>", methods=["DELETE"])
    def delete_cards(user_id):
        id = int(user_id) if user_id.isdigit() else None        
        if not id: return error_response("Missing Required Credentials", 404)    
        
        data: dict = request.get_json()
        key = data.get("key", None)

        if not key: return error_response("Missing key to delete", 400)

        filename = get_filename(id)
        cursor = DbWrite(filename=filename)  
        response = cursor.delete_from_db(key)
        if not response: return error_response("Internal Server Error", 500)
        return success_response("Resource deletion complete", 200)    



    @server.route("/new_card/<user_id>", methods=["POST"])
    def create_new_card(user_id):
        id = int(user_id) if user_id.isdigit() else user_id
        data: dict = request.get_json()
        key, value = data.get("key", None), data.get("value", None)
        
        if not id or not isinstance(id, int) or not key or not value: return error_response("Missing Required Credentials", 404)      

        # Write to db        
        filename = get_filename(id)
        cursor = DbWrite(filename=filename)        
        response = cursor.write_to_db(key, value) or False
        if not response: return error_response("Internal Server Error", 500)

        return success_response("Resource creation done", 201)    