# -*- coding: utf-8 -*-

from .tables.ambulanze import table


class Ambulanza:
    _table = table

    def __init__(self, a_dict):
        self.id_ = a_dict.get('id_')
        self.richiesta = a_dict.get('richiesta')
        self.poszione_lat = a_dict.get('posizione_lat')
        self.poszione_long = a_dict.get('poszione_long')

    def to_dict(self):
        return {
            'id_': self.id_,
            'richiesta' : self.richiesta,
            'posizione_lat' : self.poszione_lat,
            'posizione_long' : self.poszione_long,
        }
