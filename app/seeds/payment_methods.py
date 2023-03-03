from app.models import db, environment, SCHEMA, Payment


def seed_payment():
  user_1_payment_1 = Payment(
    name_on_card="Demo Lition",
    card_number="1234567891112",
    expire_month=12,
    expire_year=2026,
    cvv=123,
    card_type="Mastercard"
  )
  user_1_payment_2 = Payment(
    name_on_card="Demo Lition",
    card_number="9876543211234",
    expire_month=3,
    expire_year=2025,
    cvv=145,
    card_type="Mastercard"
  )
  user_1_payment_3 = Payment(
    name_on_card="Demo Lition",
    card_number="7894561234561",
    expire_month=10,
    expire_year=2027,
    cvv=148,
    card_type="Mastercard"
  )

  db.session.add(user_1_payment_1)
  db.session.add(user_1_payment_2)
  db.session.add(user_1_payment_3)
  db.session.commit()

def undo_comments():
  if environment == "production":
    db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
  else:
    db.session.execute("DELETE FROM payments")

  db.session.commit()
