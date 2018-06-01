# -*- coding: utf-8 -*-

from .tables.richieste_soccorso import table


class RichiestaSoccorso:
	_table = table

	def __init__(self, rs_dict):
		# entity dict
		self.e_d = rs_dict

	def to_dict(self):
		return self.e_d
