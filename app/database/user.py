# -*- coding: utf-8 -*-

from .tables.users import table

from hashlib import sha512


class User:
	_table = table

	def __init__(self, user_dict):
		self.id_ = user_dict.get('id_')
		self.email = user_dict.get('email')
		self.salt = user_dict.get('salt')
		self.password = user_dict.get('password')

	def __repr__(self):
		return 'User<id={}, email={}>'.format(self.id_, self.email)

	def is_authenticated(self):
		return False

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id_

	@property
	def password(self):
		return None

	@password.setter
	def password(self, v):
		hash = sha512()
		hash.update(('-%s-%s-' % (self.salt, v)).encode('utf-8'))
		self._password = hash.hexdigest()

	def is_valid_password(self, check_password):
		""""
		Check if the provided password is valid for the user.
		"""
		if not self.salt:
			return False

		ck_hash = sha512()
		ck_hash.update(('-%s-%s-' % (self.salt, check_password)).encode('utf-8'))
		ck_hash_password = ck_hash.hexdigest()

		return self._password == ck_hash_password
