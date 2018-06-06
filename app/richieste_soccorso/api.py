# -*- coding: utf-8 -*-

from flask import jsonify, abort, request
from flask.blueprints import Blueprint
import database as db
from flask_login import login_required, current_user
import es_gestione_ambulanze as es_ga

bp = Blueprint('richieste_soccorso', __name__)


@bp.route('/', methods=['GET'])
@login_required
def index():
    rs = []
    for c in db.get_list(db.RichiestaSoccorso, 'user_id', current_user.get_id()):
        rs.append(c.to_dict())

    return jsonify(results=rs)


@bp.route('', methods=['POST'])
@login_required
def richiesta_soccorso_intelligente():
    user_lat = request.form.get('lat')
    user_long = request.form.get('long')

    if not user_lat or not user_long:
        abort(400)

    user_d = current_user.to_dict()

    request_to_ga = {
        'user': {
            'name': user_d.get('name'),
            'surname': user_d.get('surname'),
            'location': {
                'lat': user_lat,
                'long': user_long
            }
        }
    }
    ga_response = es_ga.nuova_richiesta_soccorso(request_to_ga)

    r_d = {
        'user_id': current_user.get_id(),
        'gestione_ambulanze_richiesta_id': ga_response.get('request_id'),
        'ambulanza_associata': ga_response.get('ambulanza_associata'),
        'data': '06/06/2018',
        'stato': 'in corso'
    }
    new_request = db.RichiestaSoccorso(r_d)
    db.save(new_request)

    return jsonify(status='SUCCESS',
                   request_id=new_request.to_dict().get('id'),
                   message='Richiesta inoltrata con successo')


@bp.route('/<request_id>/stato-ambulanza', methods=['GET'])
@login_required
def stato_ambulanza(request_id):
    req = db.get(db.RichiestaSoccorso, 'id', request_id)

    if not req:
        abort(404, 'Richiesta non trovata')

    if current_user.get_id() != req.e_d.get('user_id'):
        abort(401, 'Accesso negato')

    es_ga_id = req.e_d['gestione_ambulanze_richiesta_id']

    # let's call the external service

    ga_response = es_ga.stato_ambulanza(es_ga_id)

    if ga_response['status'] == 'SUCCESS':
        return jsonify(status='SUCCESS', informazioni_ambulanza=ga_response['result'])

    if ga_response['status'] == 'ERROR' and ga_response['type'] == 'NO AMBULANZA':
        return jsonify(ga_response)

    print(ga_response)
    abort(500, 'Errore di comunicazione con il sistema di gestione ambulanze')
