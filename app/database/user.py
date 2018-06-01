# -*- coding: utf-8 -*-

from .tables.users import table

from hashlib import sha512


class User:
	_table = table

	def __init__(self, user_dict={}):
		# entity dict
		self.e_d = user_dict

		# removing password from dict and save it as hashed
		# psw = self.e_d.pop('password', "no_password_set..")
		# self._password = self.hash_password(psw)

	def __repr__(self):
		return 'User<id={}, email={}>'.format(self.e_d.get('id'), self.e_d.get('email'))

	def is_authenticated(self):
		return False

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.e_d.get('id')

	def is_valid_password(self, check_password):
		""""
		Check if the provided password is valid for the user.
		"""
		return self.e_d['password'] == check_password # self.hash_password(check_password)

	def to_dict(self):
		return self.e_d

	def hash_password(self, password):
		if not self.e_d.get('salt'):
			raise Exception('Salt for this user is lacking!', self)

		hash = sha512()
		hash.update(('-%s-%s-' % (self.e_d.get('salt'), password)).encode('utf-8'))
		return hash.hexdigest()
