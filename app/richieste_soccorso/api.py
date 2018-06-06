# -*- coding: utf-8 -*-

from flask import jsonify, abort
from flask.blueprints import Blueprint
import database as db
from flask_login import login_required, current_user
import es_gestione_ambulanze as es_ga

bp = Blueprint('richieste-soccorso', __name__)


@bp.route('/', methods=['GET'])
@login_required
def richieste_soccorso():
    rs = []
    for c in db.get_list(db.RichiestaSoccorso, 'user_id', current_user.get_id()):
        rs.append(c.to_dict())

    return jsonify(results=rs)


@bp.route('/', methods=['POST'])
@login_required
def richiesta_soccorso():
    # TODO
    return ''


@bp.route('/<int:request_id>/stato-ambulanza', methods=['GET'])
@login_required
def stato_ambulanza(request_id):
    req = db.get(db.RichiestaSoccorso, 'id', request_id)

    if current_user.get_id() != req.e_d.get('user_id'):
        abort(401, 'Accesso negato')

    if req is None:
        abort(404, 'Richiesta non trovata')

    es_ga_id = req.e_d['gestione_ambulanze_richiesta_id']

    # let's call the external service

    ga_response = es_ga.stato_ambulanza(es_ga_id)

    if ga_response['status'] == 'SUCCESS':
        # remove the id of gestione amulanze service
        return jsonify(status='SUCCESS', informazioni_ambulanza=ga_response['result'])

    print(ga_response)
    abort(500, 'Errore di comunicazione con il sistema di gestione ambulanze')
