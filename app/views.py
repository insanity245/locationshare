from app import app
from app import methods
from flask import render_template
from app import forms

# default route
@app.route('/')
def default():
	return "Yay, Flask is awesome"

# generic test
@app.route('/test')
def test():
	user = {'nickname': 'rmad'}  # fake user
	return render_template('test.html', title='Flask Home',user=user)

@app.route('/share', methods=['GET', 'POST'])
def processValidation():
	form = forms.sharestatusform(request.form)
	if request.method == 'POST' and form.validate():
		user = User(form.name.data, form.status.data)
		flash('Thanks for registering')
		return redirect('/')
	return render_template('status.html', form=form)

	# geohash test route
@app.route('/geohash')
def geohashtest():
	return methods.geohash()
