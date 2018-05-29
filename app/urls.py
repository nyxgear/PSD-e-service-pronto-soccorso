# public site imports
# import section.views / admin
import auth.api
import home.api


mounts = [
	('/', home.api),

	('/auth', auth.api)
]
