
class User:
	user = {}

	def __init__(self, user_dict):
		self.user = user_dict

	def is_authenticated(self):
		return False

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return False

