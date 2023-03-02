from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func

class Payment(db.Model):
  __tablename__ = 'payments'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}
  
  id = db.Column(db.Integer, primary_key=True)
  name_on_card = db.Column(db.String, nullable=False)
  card_number = db.Column(db.String, nullable=False)
  expire_month = db.Column(db.Integer, nullable=False)
  expire_year = db.Column(db.Integer, nullable=False)
  cvv = db.Column(db.Integer, nullable=False)
  card_type = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
  updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
  
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))

  def to_dict(self):
    return {
      "id": self.id,
      "name_on_card": self.name_on_card,
      "card_number": self.card_number,
      "expire_month": self.expire_month,
      "expire_year": self.expire_year,
      "cvv": self.cvv,
      "card_type": self.card_type
    }
