from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func

class Project(db.Model):
  __tablename__ = 'projects'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  project_name = db.Column(db.String, nullable=False)
  description = db.Column(db.Integer, nullable=False)
  story = db.Column(db.String, nullable=False)
  risks = db.Column(db.String, nullable=False)
  goal = db.Column(db.Integer, nullable=False)
  current_fund = db.Column(db.Integer, nullable=False, default=0)
  backers = db.Column(db.Integer, nullable=False, default=0)
  end_day = db.Column(db.String, nullable=False)
  project_type = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
  updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
  project_images = db.relationship("ProjectImages", back_populates="project")


  def to_dict(self):
    return {
      "id": self.id,
      "project_name": self.project_name,
      "description": self.description,
      "story": self.story,
      "risks": self.risks,
      "goal": self.goal,
      "current_fund": self.current_fund,
      "backers": self.backers,
      "end_day": self.end_day,
      "project_type": self.project_type,
      "project_images": [image.to_dict() for image in self.project_images]
    }
