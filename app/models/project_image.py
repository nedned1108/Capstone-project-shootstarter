from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func

class ProjectImages(db.Model):
  __tablename__ = 'projectImages'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  url = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
  updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

  project_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("projects.id")))
  project = db.relationship("Project", back_populates="project_images")

  def to_dict(self):
    return {
      "id": self.id,
      "url": self.url
    }
