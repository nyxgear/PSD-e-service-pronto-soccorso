# -*- coding: utf-8 -*-

from flask_login import LoginManager
import database as db

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
	return db.get(db.User, 'id_', user_id)
