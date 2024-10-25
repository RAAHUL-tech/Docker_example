from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This Flask app is running on port 5001."

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')
