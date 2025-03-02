import os
from create_app import get_app

app = get_app()

if __name__ == "__main__":
    env = os.environ.get("FLASK_ENV", "development")
    if env == "development":        
        app.run(host='0.0.0.0', port=5000)