# -*- coding: utf-8 -*-

from .tables.pratiche_assistenza import table


class PraticaAssistenza:
	_table = table

	def __init__(self, pa_dict):
		# entity dict
		self.e_d = pa_dict

	def to_dict(self):
		return self.e_d
