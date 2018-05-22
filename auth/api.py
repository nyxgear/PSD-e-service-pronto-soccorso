import flask
from flask_login import login_user
from pprint import pprint

from app import app
from database import users
from database.User import User


@app.route('/auth/login/<int:id>', methods=['POST'])
def login(id):
	# Login and validate the user.
	# user should be an instance of your `User` class
	user_dict = users.get(id)

	user = User(user_dict)

	login_user(user)

	print('User logged in successfully.')
	pprint(user_dict)

	next = flask.request.args.get('next')

	return flask.redirect(next or flask.url_for('index'))
