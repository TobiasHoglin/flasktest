from flask import Flask, render_template
import stream

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_stream', methods=['POST'])
def start_stream():
    result = stream.start_stream()
    return result

if __name__ == "__main__":
    app.run()
