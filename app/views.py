from app import app
from app import methods
from flask import render_template

# default route
@app.route('/')
def default():
	return "Yay, Flask is awesome"

# generic test
@app.route('/test')
def test():
	user = {'nickname': 'rmad'}  # fake user
	return render_template('test.html', title='Flask Home',user=user)

