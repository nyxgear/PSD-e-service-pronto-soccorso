from .tables.pronto_soccorsi import table

class ProntoSoccorso:
	_table = table

	def __init__(self, ps_dict):
		self.id_ = ps_dict.get('id_')
		self.nome_opsedale = ps_dict.get('nome_opsedale')
		self.indirizzo = ps_dict.get('indirizzo')
		self.specializzazioni = ps_dict.get('specializzazioni')
		self.distanza = ps_dict.get('distanza')

	def to_dict(self):
		return {
			'id_': self.id_,
			'nome_opsedale': self.nome_opsedale,
			'indirizzo': self.indirizzo,
			'specializzazioni': self.specializzazioni,
			'distanza': self.distanza
		}
