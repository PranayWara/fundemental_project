from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SubmitField

class CompanyFrom(FlaskForm):
    name = StringField('Input or Update the Name of video Studio Company')
    description = StringField('Add or Update a description of the Company')
    founders = StringField ('Input or Update the Name of the founder')
    submit = SubmitField()