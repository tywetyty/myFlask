from wtforms import StringField, PasswordField, BooleanField, SubmitField 
from flask.ext.wtf import Form
from wtforms.validators import Required
class NameForm(Form):
	name = StringField('What is your name?' ,validators=[Required()])
	submit = SubmitField('Submit')