# -*- coding: utf-8 -*-

from .tables.ambulanze import table


class Ambulanza:
	_table = table

	def __init__(self, a_dict):
		# entity dict
		self.e_d = a_dict

	def to_dict(self):
		return self.e_d
