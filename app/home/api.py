# -*- coding: utf-8 -*-
from flask import jsonify, url_for
from flask.blueprints import Blueprint

bp = Blueprint('home', __name__)


@bp.route("/")
def index():
    d = {
        'service_name': 'e-Service Pronto soccorso',
        'endpoints': [
            {
                'method': 'POST',
                'url': url_for('auth.login'),
                'parameters': {'email': '<string>', 'password': '<string>'}
            },
            {
                'method': 'GET',
                'url': url_for('auth.logout'),
                'parameters': {}
            },
            {
                'method': 'GET',
                'url': url_for('.index'),
                'parameters': {}
            },
            {
                'method': 'GET',
                'url': url_for('informazioni.attesa_ambulanza'),
                'parameters': {}
            },
            {
                'method': 'GET',
                'url': url_for('informazioni.pronto_soccorsi'),
                'parameters': {}
            },
            {
                'method': 'GET',
                'url': url_for('pratiche.index'),
                'parameters': {}
            },
            {
                'method': 'GET',
                'url': url_for('richieste_soccorso.index'),
                'parameters': {}
            },
            {
                'method': 'POST',
                'url': url_for('richieste_soccorso.richiesta_soccorso_intelligente'),
                'parameters': {'lat': '<float>', 'long': '<float>'}
            },
            {
                'method': 'GET',
                'url': url_for('richieste_soccorso.stato_ambulanza', request_id=u'REQUEST_ID'),
                'parameters': {'REQUEST_ID': '<int>'}
            }
        ]
    }

    return jsonify(d)
