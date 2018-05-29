import flask
from flask import jsonify
from flask.blueprints import Blueprint

bp = Blueprint('informazioni', __name__)

@bp.route('/istruzioni-attesa-ambulanza', methods=['GET'])
def istruzioni():
	d = {'Titolo': 'Cosa fare in attesa dell\'ambulanza',
		 'Informazioni': """ In attesa dell’arrivo dell'ambulanza si devono: evitare pericoli per il soccorritore, 
		 evitare ulteriori rischi per l’infortunato, evitare la ressa intorno all’infortunato. Non si deve muovere e
		 sollevare subito l’infortunato, ma farsi consigliare dall’operatore del 118, l’infermiere della
		 centrale può fornire utili consigli per prestare le prime cure, non si devono somministrare
		 bevande, soprattutto alcoliche. """
		 }

	return jsonify(d)
