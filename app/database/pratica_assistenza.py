from .tables.pratiche_assistenza import table


class PraticaAssistenza:
    _table = table

    pa_d = {}

    def __init__(self, pa_dict):
        self.pa_d = pa_dict

    def to_dict(self):
        return self.pa_d
