from flask import Blueprint, redirect,session, request
from flask_login import login_required, current_user
from app.models import db, Payment
from app.forms import PaymentForm

payment_routes = Blueprint('payment', __name__)

def validation_errors_to_error_messages(validation_errors):
  """
  Simple function that turns the WTForms validation errors into a simple list
  """
  errorMessages = []
  for field in validation_errors:
    for error in validation_errors[field]:
      errorMessages.append(f'{error}')
  return errorMessages


@payment_routes.route('/')
def get_all_payments():
  """
  Query for all payments and return them in a list of payment dictionaries
  """
  payments = Payment.query.all()
  return {"payments": [payment.to_dict() for payment in payments]}


@payment_routes.route('/', methods=["POST"])
@login_required
def post_payment():
  """
  Create a new payment and return that payment in a dictionary
  """
  form = PaymentForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    # Add and commit new project
    newPayment = Payment(
      name_on_card = form.data['name_on_card'],
      card_number = form.data['card_number'],
      expire_month = form.data['expire_month'],
      expire_year = form.data['expire_year'],
      cvv = form.data['cvv'],
      card_type = form.data['card_type'],
      user_id = current_user.id
    )
    db.session.add(newPayment)
    db.session.commit()

    return newPayment.to_dict(), 201

  if form.errors:
    return {"errors": validation_errors_to_error_messages(form.errors)}, 400


@payment_routes.route('/<int:id>', methods=["PUT"])
@login_required
def update_payment(id):
  """
  Update payment and return that payment in a dictionary
  """
  thisPayment = Payment.query.get(id)
  # thisProjectImage = ProjectImages.query.get(thisProject.project_images[0].id)
  form = PaymentForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if not thisPayment:
    return {"Error": "Payment not Found"}, 404
  if current_user.id != thisPayment.user_id:
    return {"Error": "Forbidden"}, 403

  if form.validate_on_submit():
    thisPayment.comment = form.data['payment']

    db.session.commit()

    return thisPayment.to_dict(), 200
  if form.errors:
    return {"errors": validation_errors_to_error_messages(form.errors)}, 400


@payment_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_payment(id):
  """
  Delete payment
  """
  thisPayment = Payment.query.get(id)

  if not thisPayment:
    return {"Error": "Payment not Found"}, 404
  if current_user.id != thisPayment.user_id:
    return {"Error": "Forbidden"}, 403

  db.session.delete(thisPayment)
  db.session.commit()

  return {'Message': 'The payment has been deleted!'}, 200
