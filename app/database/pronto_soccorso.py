from .table_pronto_soccorsi import table

from pprint import pprint


class ProntoSoccorso:
	_table = table

	ps_d = {}

	def __init__(self, ps_dict):
		self.ps_d = ps_dict

	def to_dict(self):
		return self.ps_d
