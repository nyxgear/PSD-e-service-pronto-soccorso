from .table_users import table


class User:
	_table = table

	user_d = {}

	def __init__(self, user_dict):
		self.user_d = user_dict

	def is_authenticated(self):
		return False

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.user_d.get('id')
