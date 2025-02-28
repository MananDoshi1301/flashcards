from flask import Flask, request, jsonify
from application.write_db import DbWrite
import os

def error_response(msg: str, code: int):
    return jsonify({"error": msg}), code    

def set_routes(server: Flask):

    @server.route("/", methods=["GET"])
    def hello():
        return "This is app!"


    @server.route("/new_card/<user_id>", methods=["POST"])
    def create_new_card(user_id):
        id = int(user_id) if user_id.isdigit() else user_id
        data: dict = request.get_json()
        key, value = data.get("key", None), data.get("value", None)
        
        if not id or not isinstance(id, int) or not key or not value: return error_response("Missing Required Credentials", 404)      

        # Write to db
        base_path = os.path.join(os.getcwd(), "data")
        filename = f"{id}_data"
        filepath: str = os.path.join(base_path, filename)
        print(filepath)
        cursor = DbWrite(filename=filepath)
        response = False
        response = cursor.write_to_db(key, value)
        if not response: return error_response("Internal Server Error", 500)

        return "Resource creation done", 200
    ...