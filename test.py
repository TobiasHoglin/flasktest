from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<button type="button">start owlcam</button>'

@ app.route('stream.py')
def stream():
    return 'now were streaming'

if __name__ == "__main__":
    app.run()