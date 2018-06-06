# -*- coding: utf-8 -*-

from .tables.richieste import table


class Richiesta:
    _table = table

    def __init__(self, rs_dict):
        # entity dict
        self.e_d = rs_dict

    def to_dict(self):
        return self.e_d
