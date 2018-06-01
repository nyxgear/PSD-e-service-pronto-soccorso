# -*- coding: utf-8 -*-

import flask
from flask import jsonify
from flask.blueprints import Blueprint
import database as db

bp = Blueprint('informazioni', __name__)


@bp.route('/attesa-ambulanza', methods=['GET'])
def attesa_ambulanza():
	d = {
		'Titolo': 'Cosa fare in attesa dell\'ambulanza',
		'Informazioni': """ In attesa dell’arrivo dell'ambulanza si devono: evitare pericoli per il soccorritore, 
		 evitare ulteriori rischi per l’infortunato, evitare la ressa intorno all’infortunato. Non si deve muovere e
		 sollevare subito l’infortunato, ma farsi consigliare dall’operatore del 118, l’infermiere della
		 centrale può fornire utili consigli per prestare le prime cure, non si devono somministrare
		 bevande, soprattutto alcoliche. """
	}

	return jsonify(d)


@bp.route('/pronto-soccorsi', methods=['GET'])
def pronto_soccorsi():
	ps_list = [c.to_dict() for c in db.get_list(db.ProntoSoccorso)]
	return jsonify(results=ps_list)
