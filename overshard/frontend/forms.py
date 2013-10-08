
from flask.ext.wtf import Form 
from wtforms import TextField
from wtforms.validators import DataRequired


class MyForm(Form):
	username=TextField("username",validators=[DataRequired()])