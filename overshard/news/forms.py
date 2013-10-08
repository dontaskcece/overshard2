from flask.ext.wtf import Form 
from wtforms import TextField
from wtforms.validators import DataRequired



class WriteForm(Form):
	content=TextField("content",validators=[DataRequired])