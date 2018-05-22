from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
	return 'Index Page'


@app.route('/hello')
def hello():
	return 'Hello, World'


@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return 'Post %d' % post_id
