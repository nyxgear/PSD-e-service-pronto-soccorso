# -*- coding: utf-8 -*-

import flask
from flask import jsonify
from flask.blueprints import Blueprint
import database as db
from flask_login import login_required, current_user

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


@bp.route('/<int:request_id>/stato-ambulanza', methods=['GET'])
@login_required
def stato_ambulanza(request_id):
    # pa_list = [c.to_dict() for c in
    #            db.get_list(db.PraticaAssistenza, 'user_id', 1)]

    sa_list = []
    for c in db.get_list(db.Ambulanza, 'user_id', current_user.get_id()):
       sa_list.append(c.to_dict())



    return jsonify(results=sa_list)