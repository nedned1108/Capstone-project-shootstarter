from app.models import db, environment, SCHEMA, Project


def seed_projects():
  ascension_tactics = Project(
    project_name="Ascension Tactics Inferno",
    description="The standalone expansion to the wildly popular Ascension Tactics game. Funded in 4 minutes!",
    story="""
      Ascension Tactics pioneered a brand-new genre to critical acclaim by combining
      the best of tactical miniatures games with the fast-paced strategy of deck-building
      games. The most iconic characters from the award-winning deck-building game were
      brought to life as highly-detailed paintable 3D miniatures.
    """,
    risks="""
    Producing projects like this isn't easy. COVID related delays, delays in shipping and
    global logistics may all delay the production of this game.
    We've learned a lot over the years and are building in safeguards to
    ensure that products are delivered ontime and at a high quality to backers.
    """,
    goal=20000,
    current_fund=0,
    backers=0,
    end_day="March 1st 2023",
    project_type="game",
    user_id=1
  )
  make_100 = Project(
    project_name='Make 100 - "Unforgotten" Handmade Pendants by Sprite',
    description="I'm making pendants that immortalize and honor natures magic and creatures. I can't wait to share them with you!",
    story="""
      I'm creating pendants that are a combination of my favorite things, drawing,
      sculpture and bits of all of the magical items I've collected. This is my way to immortalize
      and honor the washed up forgotten souls I find under foot on my nature walks.
    """,
    risks="""
    This is my first Kickstarter and it's a project close to my heart.
    Each piece is handmade by me and is one-of-a-kind.
    While these take time and great care to make I am confident I will have my rewards shipped by early May.
    I will keep you updated along the way. Thank you friends. <3
    """,
    goal=900,
    current_fund=0,
    backers=0,
    end_day="March 25 2023",
    project_type="art",
    user_id=2
  )

  db.session.add(ascension_tactics)
  db.session.add(make_100)
  db.session.commit()


def undo_projects():
  if environment == "production":
    db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
  else:
    db.session.execute("DELETE FROM projects")

  db.session.commit()
