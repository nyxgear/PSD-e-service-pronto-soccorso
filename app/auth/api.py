from flask import request, jsonify
from flask.blueprints import Blueprint
from pprint import pprint


bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['POST'])
def login():
	credentials = request.json

	# Login and validate the user.
	# # user should be an instance of your `User` class
	# user_dict = users.get(id)
	#
	# user = User(user_dict)
	#
	# login_user(user)
	#
	# print('User logged in successfully.')
	# pprint(user_dict)
	#
	# next = flask.request.args.get('next')

	return jsonify(credentials)
