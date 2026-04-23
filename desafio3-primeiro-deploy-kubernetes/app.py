from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    return f"<h1>Hello World!</h1><p>Rodando no Pod: {hostname}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)