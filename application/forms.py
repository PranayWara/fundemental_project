from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.core import SelectField

class CompanyFrom(FlaskForm):
    name = StringField('Input or Update the Name of video Studio Company')
    description = StringField('Add or Update a description of the Company')
    founders = StringField ('Input or Update the Name of the founder')
    submit = SubmitField()

class GamesForm(FlaskForm):
    name = StringField('Input or Update the Name of the Game')
    genre = StringField('Add or Update the genre of the Game')
    company = SelectField('Choose a Company', choices=[])
    submit = SubmitField()