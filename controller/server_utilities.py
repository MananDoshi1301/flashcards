from flask import jsonify

def error_response(msg: str, code: int):
    return jsonify({"error": msg}), code    

def success_response(msg: str, code: int, **kwargs):
    package = {"message": msg}
    for k, v in kwargs.items(): package[k] = v
    
    return jsonify(package), code

def get_filename(user_id: int) -> str:
    filename: str = f"{user_id}_data"  
    return filename