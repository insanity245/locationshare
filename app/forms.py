from wtforms import Form, TextField, validators

class RegistrationForm(Form):
	name = TextField('name', [validators.Length(min=2, max=25)])
	status = TextField('status', [validators.Length(min=6, max=350)])
