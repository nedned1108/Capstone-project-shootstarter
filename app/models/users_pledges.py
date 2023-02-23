from .db import db, environment, SCHEMA, add_prefix_for_prod


users_pledges = db.Table(
  "users_pledges",
  db.Column("user_id", db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), primary_key=True),
  db.Column("pledge_id", db.Integer, db.ForeignKey(add_prefix_for_prod("pledges.id")), primary_key=True)
)

if environment == "production":
    __table_args__ = {'schema': SCHEMA}
    users_pledges = db.Table(
      "users_pledges",
      db.Column("user_id", db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), primary_key=True),
      db.Column("pledge_id", db.Integer, db.ForeignKey(add_prefix_for_prod("pledges.id")), primary_key=True)
    )
