# -*- coding: utf-8 -*-

import os
from flask import Flask, g, request, url_for

import config
import database
import auth
import urls

app = Flask(__name__, static_url_path='')
app.debug = config.DEBUG
app.secret_key = config.SECRET_KEY

# Auth
auth.login_manager.init_app(app)


@app.context_processor
def inject_custom():
	d = {'SITE_TITLE': config.SITE_TITLE}
	return d


for (mount_position, mount_module) in urls.mounts:
	app.register_blueprint(mount_module.bp, url_prefix=mount_position)

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 5000))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)
