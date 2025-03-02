from create_app import get_app

if __name__ == "__main__":
    PORT = 5000
    server = get_app()
    server.run(host='0.0.0.0', port=5000)