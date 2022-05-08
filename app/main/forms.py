import imp
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired
from wtforms.fields.choices import SelectField

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    title = StringField('Comment title')
    comment = TextAreaField('Pitch comment')
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category = SelectField('Add pitch category',choices = [('Pick-up Lines','Pick-up Lines'),('Sales','Sales'),('Innovation','Innovation'),('Humanity','Humanity'),('Music','Music'),('Tech','Tech')]) 
    context = TextAreaField('Pitch itself')
    submit = SubmitField('Submit')

