from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
  comment = TextAreaField('comment', validators=[DataRequired()])
  project_id = IntegerField('project_id', validators=[DataRequired()])
