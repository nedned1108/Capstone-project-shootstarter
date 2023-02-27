from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func

class Comment(db.Model):
  __tablename__ = 'comments'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  comment = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
  updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
  project_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("project.id")))

  def to_dict(self):
    return {
      "id": self.id,
      "comment": self.comment,
      "user_id": self.user_id,
      "project_id": self.project_id
    }
