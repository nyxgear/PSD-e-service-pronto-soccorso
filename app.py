from flask import Flask, request, json, jsonify

import config
from auth import login_manager

# App instantiated
app = Flask(__name__)

# Set secret key
app.secret_key = config.SECRET_KEY

# Login manager bound
login_manager.init_app(app)

from auth import api

@app.route('/')
def index():
	return 'Index Page'


@app.route('/hello')
def hello():
	return 'Hello, World'


@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return 'Post %d' % post_id


@app.route('/requests/<int:request_id>', methods=['POST'])
def post_requests(request_id):
	body_request = json.loads(request.data)

	print ('ANTONELLLA MANNAGGGGGGGIA')

	return jsonify(body_request)
