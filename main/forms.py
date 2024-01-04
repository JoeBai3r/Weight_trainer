from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField

class CreateBodybuilding(FlaskForm):
    title = StringField('Title')
    age = IntegerField('Age')
    gender = SelectField('Sex', choices=[('M', 'Male'), ('F', 'Female')])
    benchMax = IntegerField('Bench Max')
    squatMax = IntegerField('Squat Max')
    deadliftMax = IntegerField('Deadlift Max')
    submit = SubmitField('Submit')

class CreatePowerlifting(FlaskForm):
    title = StringField('Title')
    age = IntegerField('Age')
    gender = SelectField('Sex', choices=[('M', 'Male'), ('F', 'Female')])
    benchMax = IntegerField('Bench Max')
    squatMax = IntegerField('Squat Max')
    deadliftMax = IntegerField('Deadlift Max')
    submit = SubmitField('Submit')

