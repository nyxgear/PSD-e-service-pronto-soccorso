# -*- coding: utf-8 -*-

from .tables.users import table

from hashlib import sha512


class User:
	_table = table

	def __init__(self, user_dict={}):
		# entity dict
		self.e_d = user_dict
		self.password = self.e_d.pop('password', "no_password_set..")

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

	@property
	def password(self):
		# let's do not return the password :)
		return None

	@password.setter
	def password(self, v):
		if not self.e_d.get('salt'):
			raise Exception('Salt for this user is lacking!', self)

		hash = sha512()
		hash.update(('-%s-%s-' % (self.e_d.get('salt'), v)).encode('utf-8'))
		self._password = hash.hexdigest()

	def is_valid_password(self, check_password):
		""""
		Check if the provided password is valid for the user.
		"""
		if not self.e_d.get('salt'):
			return False

		ck_hash = sha512()
		ck_hash.update(
			('-%s-%s-' % (self.e_d.get('salt'), check_password)).encode('utf-8'))
		ck_hash_password = ck_hash.hexdigest()

		return self._password == ck_hash_password

	def to_dict(self):
		return self.e_d
