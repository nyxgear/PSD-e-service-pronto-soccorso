# public site imports
# import section.views / admin
import auth.api
import home.api
import informazioni.api

mounts = [
	('/', home.api),

	('/auth', auth.api),

	('/informazioni', informazioni.api)
]
