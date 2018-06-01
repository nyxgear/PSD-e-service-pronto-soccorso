# -*- coding: utf-8 -*-

from .tables.pronto_soccorsi import table


class ProntoSoccorso:
	_table = table

	def __init__(self, ps_dict):
		# entity dict
		self.e_d = ps_dict

	def to_dict(self):
		return self.e_d
