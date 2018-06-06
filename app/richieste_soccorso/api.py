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
    # pa_list = [c.to_dict() for c in
    #            db.get_list(db.PraticaAssistenza, 'user_id', 1)]

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
    print(req.to_dict())
    if req is None:
        abort(404, 'Richiesta non trovata')
    sa = es_ga.stato_ambulanza(req.e_d['gestione_ambulanze_richiesta_id'])
    print(sa.to_dict())
    return jsonify(results=sa)
