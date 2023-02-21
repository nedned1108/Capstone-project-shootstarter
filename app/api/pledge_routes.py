from flask import Blueprint, redirect,session, request
from flask_login import login_required, current_user
from app.models import db, Pledge
from app.forms import PledgeForm

pledge_routes = Blueprint('pledge', __name__)

def validation_errors_to_error_messages(validation_errors):
  """
  Simple function that turns the WTForms validation errors into a simple list
  """
  errorMessages = []
  for field in validation_errors:
    for error in validation_errors[field]:
      errorMessages.append(f'{field} : {error}')
  return errorMessages
