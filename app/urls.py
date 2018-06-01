# -*- coding: utf-8 -*-

# public site imports
# import section.views / admin
import auth.api
import home.api
import informazioni.api
import pratiche.api
import richieste_soccorso.api

mounts = [
	('/', home.api),

	('/auth', auth.api),

	('/informazioni', informazioni.api),

	('/pratiche', pratiche.api),

	('/richieste-soccorso', richieste_soccorso.api)
]
