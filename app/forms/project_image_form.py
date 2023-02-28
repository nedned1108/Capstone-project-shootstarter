from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, URL
# from app.models import ProjectImages


class ProjectImageForm(FlaskForm):
  url = StringField('url', validators=[DataRequired(message="Image is required"), URL(message="Image is not url")])
  project_id = IntegerField('project_id', validators=[DataRequired()])
