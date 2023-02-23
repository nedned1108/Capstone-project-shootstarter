from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, Length, URL
# from app.models import Project


class ProjectForm(FlaskForm):
  project_name = StringField('store_name', validators=[DataRequired(), Length(max=100)])
  description = StringField('description', validators=[DataRequired()])
  story = TextAreaField('story', validators=[DataRequired()])
  risks = TextAreaField('risks', validators=[DataRequired()])
  goal = IntegerField('goal', validators=[DataRequired(), NumberRange(min=1, max=1000000, message="Goal must be between 1 and 1,000,000")])
  current_fund = IntegerField('current_fund', default=0)
  backers = IntegerField('backers', default=0)
  end_day = StringField('end_day', validators=[DataRequired()])
  project_type = StringField('project_type', validators=[DataRequired()])
  url = StringField('url', validators=[DataRequired(), URL()])
  # owner_id = IntegerField('owner_id', validators=[DataRequired()])
