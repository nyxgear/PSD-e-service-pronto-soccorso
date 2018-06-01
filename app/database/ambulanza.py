# -*- coding: utf-8 -*-

from .tables.ambulanze import table


class Ambulanza:
    _table = table

    def __init__(self, a_dict):
        self.id_ = a_dict.get('id_')
        self.user_id = a_dict.get('user_id')
        self.stato = a_dict.get('stato')
        self.posizione = a_dict.get('posizione')

    def to_dict(self):
        return {
            'id_': self.id_,
            'user_id': self.user_id,
            'stato': self.stato,
            'poszione': self.posizione,
        }
