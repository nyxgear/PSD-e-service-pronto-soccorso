# -*- coding: utf-8 -*-

from .tables.richieste_soccorso import table


class RichiestaSoccorso:
    _table = table

    def __init__(self, rs_dict):
        self.id_ = rs_dict.get('id_')
        self.user_id = rs_dict.get('user_id')
        self.data = rs_dict.get('data')
        self.stato = rs_dict.get('stato')
        self.ambulanza = rs_dict.get('ambulanza')


    def to_dict(self):
        return {
            'id_': self.id_,
            'user_id': self.user_id,
            'data': self.data,
            'stato': self.stato,
            'ambulanza': self.ambulanza,
        }
