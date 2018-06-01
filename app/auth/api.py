# -*- coding: utf-8 -*-

from flask import request, jsonify, abort
from flask.blueprints import Blueprint

import database as db
from flask_login import login_user

bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['POST'])
def login():
	res = {'status': 'ERROR', 'message': 'Invalid user or password'}

	email = request.form.get('email')
	password = request.form.get('password')

	# not valid parameters or malformed request
	if not email or not password:
		abort(400)

	user = db.get(db.User, "email", email)

	if not user:
		return jsonify(res)

	if not user.is_valid_password(password):
		return jsonify(res)

	# set the current logged in user to flask_login
	login_user(user)
	res['status'] = 'SUCCESS'
	res['message'] = 'Login successfully done'

	return jsonify(res)
