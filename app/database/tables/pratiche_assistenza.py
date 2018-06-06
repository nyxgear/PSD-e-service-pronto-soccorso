# -*- coding: utf-8 -*-

table = [
    {
        'id': 1,
        'user_id': 1,
        'data': '12/03/2018',
        'pronto_soccorso': 'Niguarda',
        'codice_colore': 'verde',
        'ticket': {
            'id': '156CBF',
            'titolo': 'Pagamento assistenza PS',
            'download_url': 'https://cdn.ospedaleniguarda.it/downloads/156CBF.pdf'
        },
        'referto': {},
        'ricetta': {}
    },
    {
        'id': 2,
        'user_id': 2,
        'data': '12/03/2018',
        'pronto_soccorso': 'Fatebenefratelli',
        'codice_colore': 'bianco',
        'ticket': '156CBF',
        'referto': 'None',
        'ricetta': 'None'
    },
    {
        'id': 3,
        'user_id': 2,
        'data': '12/03/2018',
        'pronto_soccorso': 'Fatebenefratelli',
        'codice_colore': 'verde',
        'ticket': {
            'id': '156CBF',
            'titolo': 'Pagamento assistenza PS',
            'download_url': 'https://cdn.fatebenefratelli.it/downloads/156CBF.pdf'
        },
        'referto': 'None',
        'ricetta': {
            'id': '777AAA',
            'titolo': 'Pagamento assistenza PS',
            'download_url': 'https://cdn.cup.regione.lombardia.it/downloads/777AAA.pdf'
        }
    }
]
