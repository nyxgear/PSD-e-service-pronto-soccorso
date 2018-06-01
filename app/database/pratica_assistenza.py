# -*- coding: utf-8 -*-

from .tables.pratiche_assistenza import table


class PraticaAssistenza:
	_table = table

	def __init__(self, pa_dict):
		self.id_ = pa_dict.get('id_')
		self.user_id = pa_dict.get('user_id')
		self.data = pa_dict.get('data')
		self.pronto_soccorso = pa_dict.get('pronto_soccorso')
		self.codice_colore = pa_dict.get('codice_colore')
		self.ticket = pa_dict.get('ticket')
		self.referto = pa_dict.get('referto')
		self.ricetta = pa_dict.get('ricetta')

	def to_dict(self):
		return {
			'id_': self.id_,
			'user_id': self.user_id,
			'data': self.data,
			'pronto_soccorso': self.pronto_soccorso,
			'codice_colore': self.codice_colore,
			'ticket': self.ticket,
			'referto': self.referto,
			'ricetta': self.ricetta
		}
