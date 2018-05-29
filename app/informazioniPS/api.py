import flask
from flask import jsonify
from flask.blueprints import Blueprint
import database as db


bp = Blueprint('informazioniPS', __name__)


@bp.route('/', methods=['GET'])
def informazioniPS():
	l=db.get_list(db.ProntoSoccorso)

	return jsonify(l)
