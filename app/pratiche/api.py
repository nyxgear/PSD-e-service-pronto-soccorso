import flask
from flask import jsonify
from flask.blueprints import Blueprint
import database as db
from flask_login import login_required, current_user

bp = Blueprint('pratiche', __name__)


@bp.route('/', methods=['GET'])
@login_required
def pratiche_assistenza():
	# pa_list = [c.to_dict() for c in
	#            db.get_list(db.PraticaAssistenza, 'user_id', 1)]

	pa_list = []
	for c in db.get_list(db.PraticaAssistenza, 'user_id', current_user.get_id()):
		pa_list.append(c.to_dict())

	return jsonify(results=pa_list)
