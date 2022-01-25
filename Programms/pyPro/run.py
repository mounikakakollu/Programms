from flask import Flask, jsonify, make_response, render_template, request
from flask_cors import CORS, cross_origin
from controllers import api
from controllers import *

app = Flask(__name__, template_folder='app/templates/', static_folder='app/static')
CORS(app)
app.register_blueprint(api, url_prefix='/api/v1')

@app.route('/health_check')
def health_check():
    return 'success'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/practice')
def practice():
    return render_template('practice.html')
