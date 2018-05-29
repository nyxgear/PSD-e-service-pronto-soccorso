from .table_pronto_soccorsi import table
from pprint import pprint


class ProntoSoccorso:
    _table = table

    ps_d = {}

    def __init__(self, ps_dict):
        self.ps_d = ps_dict

    def __repr__(self):
        return str(pprint(self.ps_d))
