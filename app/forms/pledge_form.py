from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length, URL
from app.models import Pledge


class ProjectForm(FlaskForm):
  pledge_name = StringField('pledge_name', validators=[DataRequired(), Length(max=100)])
  price = IntegerField('price', validators=[DataRequired(), NumberRange(min=1, max=1000000)])
  ships_to = StringField('ships_to', validators=[DataRequired()])
  rewards = StringField('rewards', validators=[DataRequired()])
  estimated_delivery = StringField('estimated_delivery', validators=[DataRequired()])

