from flask import Blueprint, redirect,session, request
from flask_login import login_required, current_user
from app.models import db, Project, ProjectImages


project_routes = Blueprint('project', __name__)

def validation_errors_to_error_messages(validation_errors):
  """
  Simple function that turns the WTForms validation errors into a simple list
  """
  errorMessages = []
  for field in validation_errors:
      for error in validation_errors[field]:
          errorMessages.append(f'{field} : {error}')
  return errorMessages


@project_routes.route('/')
def get_all_projects():
  """
  Query for all projects an return them in a list of project dictionaries
  """
  projects = Project.query.all()
  return {"projects": [project.to_dict() for project in projects]}


@project_routes.route('/', methods=["POST"])
@login_required
def post_project():
  """
  Create a new project and return that project in a dictionary
  """
