from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length


class PaymentForm(FlaskForm):
  name_on_card = StringField('name_on_card', validators=[DataRequired(message="Name on card is required")])
  card_number = StringField('card_number', validators=[DataRequired(message="Card number is required"), Length(min=12, max=12, message="Invalid Card Number")])
  expire_month = IntegerField('expire_month', validators=[DataRequired(message="Expire month is required"), NumberRange(min=1, max=12, message="Invalid Expiration Date")])
  expire_year = IntegerField('expire_year', validators=[DataRequired(message="Expire year is required")])
  cvv = IntegerField('cvv', validators=[DataRequired(message="CVV is required")])
  card_type = StringField('card_type', validators=[DataRequired(message="Card type is required")])
