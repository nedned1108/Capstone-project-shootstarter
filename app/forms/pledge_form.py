from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length
# from app.models import Pledge


class PledgeForm(FlaskForm):
  pledge_name = StringField('pledge_name', validators=[DataRequired(message="Pledge name is required"), Length(max=100, message="Pledge name must be less than 100 characters")])
  price = IntegerField('price', validators=[DataRequired(), NumberRange(min=1, max=10000000, message="Price must be less than 10,000,000")])
  ships_to = StringField('ships_to', validators=[DataRequired(message="Ship is required")])
  rewards = StringField('rewards', validators=[DataRequired(message="Reward is required")])
  estimated_delivery = StringField('estimated_delivery', validators=[DataRequired(message="Estimated delivery is required")])
