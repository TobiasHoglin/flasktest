from flask import Flask, render_template
#import stream
import test
#from stream_test_lib import *
import subprocess

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def stream():
    return render_template('stream.html') 


#@app.route('/stream', methods=['GET','POST'])
#def start_stream():
#   return stream.start_stream()


    

if __name__ == "__main__":
    app.run()