# public site imports
# import section.views / admin
import auth.api
import home.api
import informazioni.api
import informazioniPS.api

mounts = [
	('/', home.api),

	('/auth', auth.api),

	('/informazioni', informazioni.api),

	('/informazioniPS', informazioniPS.api),
]
