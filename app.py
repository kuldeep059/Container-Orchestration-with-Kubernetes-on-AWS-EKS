from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = os.environ.get('HOSTNAME', 'localhost')
    return f'Hello from my Flask app running on {hostname}!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)