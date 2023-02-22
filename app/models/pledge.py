from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func
from .users_pledges import users_pledges

class Pledge(db.Model):
  __tablename__ = 'pledges'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  pledge_name = db.Column(db.String, nullable=False)
  price = db.Column(db.Integer, nullable=False)
  ships_to = db.Column(db.String, nullable=False)
  rewards = db.Column(db.String, nullable=False)
  estimated_delivery = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
  updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

  project_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("projects.id")))
  users = db.relationship("User", secondary=users_pledges, back_populates="pledges")

  def to_dict(self):
    return {
      "id": self.id,
      "pledge_name": self.pledge_name,
      "price": self.price,
      "ships_to": self.ships_to,
      "rewards": self.rewards,
      "estimated_delivery": self.estimated_delivery,
      # "total_user": len(list(self.users.items))
    }
