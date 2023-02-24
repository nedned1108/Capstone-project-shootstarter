from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class ChoosePledgeForm(FlaskForm):
  user_id = IntegerField('user_id', validators=[DataRequired()])
  pledge_id = IntegerField('pledge_id', validators=[DataRequired()])
