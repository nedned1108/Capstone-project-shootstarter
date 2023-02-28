from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, Length, URL
# from app.models import Project


class ProjectForm(FlaskForm):
  project_name = StringField('store_name', validators=[DataRequired(message="Project name is required"), Length(max=100, message="Project name must be less than 100 characters")])
  description = StringField('description', validators=[DataRequired(message="Description is required")])
  story = TextAreaField('story', validators=[DataRequired(message="Story is required")])
  risks = TextAreaField('risks', validators=[DataRequired(message="Risks is required")])
  goal = IntegerField('goal', validators=[DataRequired(message="Goal is required"), NumberRange(min=1, max=10000000, message="Goal must be between 1 and 10,000,000")])
  current_fund = IntegerField('current_fund', default=0)
  backers = IntegerField('backers', default=0)
  end_day = StringField('end_day', validators=[DataRequired(message="End day is required")])
  project_type = StringField('project_type', validators=[DataRequired(message="Project type is required")])
  url = StringField('url', validators=[DataRequired(message="Image is required"), URL(message="Image is not url")])
  # owner_id = IntegerField('owner_id', validators=[DataRequired()])
