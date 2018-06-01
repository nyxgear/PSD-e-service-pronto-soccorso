# -*- coding: utf-8 -*-

from flask import jsonify, json, request
from flask.blueprints import Blueprint


bp = Blueprint('home', __name__)

@bp.route("/")
def index():

	return "Test"

@bp.route('/hello')
def hello():
	return 'Hello, World'


@bp.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return 'Post %d' % post_id


@bp.route('/requests/<int:request_id>', methods=['POST'])
def post_requests(request_id):
	body_request = json.loads(request.data)

	print ('Test :D')

	return jsonify(body_request)


