from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired

class PredictionForm(FlaskForm):
    year_of_construction = IntegerField('Année de construction', validators=[DataRequired(message="L'année de construction est requise!")])
    num_observations = IntegerField('Nombre d\'observations', validators=[DataRequired(message="Le nombre n'observations est reqiose!")])
    surface_area = FloatField('Surface habitable', validators=[DataRequired(message="La surface est requise!")])
    submit = SubmitField('Prédire')
