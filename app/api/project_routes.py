from flask import Blueprint, redirect,session, request
from flask_login import login_required, current_user
from app.models import db, Project, ProjectImages, Pledge
from app.forms import ProjectForm, ProjectImageForm, PledgeForm, ChoosePledgeForm
from datetime import datetime, date

project_routes = Blueprint('project', __name__)

def validation_errors_to_error_messages(validation_errors):
  """
  Simple function that turns the WTForms validation errors into a simple list
  """
  errorMessages = []
  for field in validation_errors:
    for error in validation_errors[field]:
      errorMessages.append(f'{error}')
  return errorMessages


@project_routes.route('/')
def get_all_projects():
  """
  Query for all projects and return them in a list of project dictionaries
  """
  projects = Project.query.all()
  return {"projects": [project.to_dict() for project in projects]}


@project_routes.route('/', methods=["POST"])
@login_required
def post_project():
  """
  Create a new project and return that project in a dictionary
  """
  form = ProjectForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  
  # today = date.today()
  # end_day = datetime.strptime(form.data['end_day'], '%Y-%m-%d').date()
  # if end_day <= today:
  #   return {"errors": "end day can not be today or in the past"}, 400
  
  if form.validate_on_submit():

    # Add and commit new project
    newProject = Project(
      project_name = form.data['project_name'],
      description = form.data['description'],
      story = form.data['story'],
      risks = form.data['risks'],
      goal = form.data['goal'],
      current_fund = form.data['current_fund'],
      backers = form.data['backers'],
      end_day = form.data['end_day'],
      project_type = form.data['project_type'],
      owner_id = current_user.id
    )
    db.session.add(newProject)
    db.session.commit()
    # Add and commit project image
    newProjectImage = ProjectImages(
      url = form.data['url'],
      project_id = newProject.id
    )
    db.session.add(newProjectImage)
    db.session.commit()

    return newProject.to_dict(), 201

  if form.errors:
    return {"errors": validation_errors_to_error_messages(form.errors)}, 400


@project_routes.route('/<int:id>')
def get_project(id):
  """
  Query for a project by id and returns that project in a dictionary
  """
  thisProject = Project.query.get(id)

  if not thisProject:
    return {'Error': 'Project not Found'}, 404

  return thisProject.to_dict(), 200


@project_routes.route('/<int:id>', methods=["PUT"])
@login_required
def update_project(id):
  """
  Update project and return that project in a dictionary
  """
  thisProject = Project.query.get(id)
  # thisProjectImage = ProjectImages.query.get(thisProject.project_images[0].id)
  form = ProjectForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if not thisProject:
    return {"Error": "Project not Found"}, 404
  if current_user.id != thisProject.owner_id:
    return {"Error": "Forbidden"}, 403

  if form.validate_on_submit():
    thisProject.project_name = form.data['project_name']
    thisProject.description = form.data['description']
    thisProject.story = form.data['story']
    thisProject.risks = form.data['risks']
    thisProject.goal = form.data['goal']
    thisProject.end_day = form.data['end_day']
    thisProject.project_type = form.data['project_type']

    db.session.commit()

    return thisProject.to_dict(), 200
  if form.errors:
    return {"errors": validation_errors_to_error_messages(form.errors)}, 400


@project_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_project(id):
  """
  Delete project
  """
  thisProject = Project.query.get(id)

  if not thisProject:
    return {"Error": "Project not Found"}, 404
  if current_user.id != thisProject.owner_id:
    return {"Error": "Forbidden"}, 403

  db.session.delete(thisProject)
  db.session.commit()

  return {'Message': 'The project has been deleted!'}, 200


@project_routes.route('/<int:id>/images', methods=["POST"])
@login_required
def post_project_image(id):
  """
  Add new project images
  """
  form = ProjectImageForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    newProjectImage = ProjectImages(
      url = form.data['url'],
      project_id = id
    )
    db.session.add(newProjectImage)
    db.session.commit()

    return {"Message": "Images added successfully"}, 201

  if form.errors:
    return {"errors": validation_errors_to_error_messages(form.errors)}, 400


@project_routes.route('/<int:id>/pledges', methods=["POST"])
@login_required
def post_pledge(id):
  """
  Create a new pledge and return that pledge in a dictionary
  """
  project = Project.query.get(id)
  if not project:
    return {"errors": "Project not found"}, 404
  if current_user.id != project.owner_id:
    return {"errors": "Forbidden"}, 403
  
  form = PledgeForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    newPledge = Pledge(
      pledge_name = form.data['pledge_name'],
      price = form.data['price'],
      ships_to = form.data['ships_to'],
      rewards = form.data['rewards'],
      estimated_delivery = form.data['estimated_delivery'],
      project_id = id,
      owner_id = current_user.id
    )
    db.session.add(newPledge)
    db.session.commit()
    return newPledge.to_dict(), 201

  if form.errors:
    return {"errors": validation_errors_to_error_messages(form.errors)}, 400
