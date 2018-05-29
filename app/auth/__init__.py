from flask_login import LoginManager
from database import users

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)
