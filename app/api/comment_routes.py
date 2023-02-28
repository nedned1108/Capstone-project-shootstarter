from flask import Blueprint, redirect,session, request
from flask_login import login_required, current_user
from app.models import db, Comment
from app.forms import CommentForm

comment_routes = Blueprint('comment', __name__)

def validation_errors_to_error_messages(validation_errors):
  """
  Simple function that turns the WTForms validation errors into a simple list
  """
  errorMessages = []
  for field in validation_errors:
    for error in validation_errors[field]:
      errorMessages.append(f'{field} : {error}')
  return errorMessages


@comment_routes.route('/')
def get_all_comments():
  """
  Query for all comments and return them in a list of comment dictionaries
  """
  comments = Comment.query.all()
  return {"comments": [comment.to_dict() for comment in comments]}


@comment_routes.route('/', methods=["POST"])
@login_required
def post_comment():
  """
  Create a new comment and return that comment in a dictionary
  """
  form = CommentForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    # Add and commit new project
    newComment = Comment(
      comment = form.data['comment'],
      project_id = form.data['project_id'],
      user_id = current_user.id
    )
    db.session.add(newComment)
    db.session.commit()

    return newComment.to_dict(), 201

  if form.errors:
    return {"errors": validation_errors_to_error_messages(form.errors)}, 400


@comment_routes.route('/<int:id>', methods=["PUT"])
@login_required
def update_comment(id):
  """
  Update comment and return that comment in a dictionary
  """
  thisComment = Comment.query.get(id)
  # thisProjectImage = ProjectImages.query.get(thisProject.project_images[0].id)
  form = CommentForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if not thisComment:
    return {"Error": "Comment not Found"}, 404
  if current_user.id != thisComment.user_id:
    return {"Error": "Forbidden"}, 403

  if form.validate_on_submit():
    thisComment.comment = form.data['comment']

    db.session.commit()

    return thisComment.to_dict(), 200
  if form.errors:
    return {"errors": validation_errors_to_error_messages(form.errors)}, 400


@comment_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_comment(id):
  """
  Delete comment
  """
  thisComment = Comment.query.get(id)

  if not thisComment:
    return {"Error": "Comment not Found"}, 404
  if current_user.id != thisComment.user_id:
    return {"Error": "Forbidden"}, 403

  db.session.delete(thisComment)
  db.session.commit()

  return {'Message': 'The comment has been deleted!'}, 200
