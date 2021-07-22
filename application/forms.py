from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, Length, ValidationError



class CompanyFrom(FlaskForm):
    name = StringField('Input or Update the Name of video Studio Company', validators=[
        DataRequired()])
    description = StringField('Add or Update a description of the Company')
    founders = StringField ('Input or Update the Name of the founder')
    submit = SubmitField()

class GamesForm(FlaskForm):
    name = StringField('Input or Update the Name of the Game', validators=[
        DataRequired()])
    genre = StringField('Add or Update the genre of the Game')
    company = SelectField('Choose a Company', choices=[])
    submit = SubmitField()