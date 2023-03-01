from app.models import db, environment, SCHEMA, Comment


def seed_comments():
  ascension_comment1 = Comment(
    comment="Wish can you add runes and power tracker . Its really helpful during the game",
    project_id=1,
    user_id=3
  )
  ascension_comment2 = Comment(
    comment="The Wretched look so cool! Thats a great idea to incorporate into the game. How does psychic link work? Will there be 4 wretched mini’s, one for each card?",
    project_id=1,
    user_id=4
  )
  ascension_comment3 = Comment(
    comment="Seeing this new (5th) custom started deck got me thinking about a possible add on. Way, way back in original ascension there was a Kickstarter Zombie starter Deck that was so cool. Any thought of brining something like that back as an add on for your long term players haha",
    project_id=1,
    user_id=5
  )
  ascension_comment4 = Comment(
    comment="Very nice!!!",
    project_id=1,
    user_id=2
  )
  make_100_comment1 = Comment(
    comment="Your story was so moving! I also collected little things when I was a kid andddd I still do!!! Haha love it!",
    project_id=2,
    user_id=1
  )
  make_100_comment2 = Comment(
    comment="I saw the update thanks!",
    project_id=2,
    user_id=3
  )
  make_100_comment3 = Comment(
    comment="So bummed I missed this!",
    project_id=2,
    user_id=5
  )
  revopoint_comment1 = Comment(
    comment="Wholeheartedly agreed, a calibration board should be part of the package. We are paying much more than your other projects. What's so hard about including one? You could make it like the monopoly game board.",
    project_id=3,
    user_id=3
  )
  revopoint_comment2 = Comment(
    comment="Hello there! I'm just merely curious. Is the roadmap a fixed timeline? Or is there any chance now that the pladged goal is an early success, that the manufacturing / delivering will start earlier?",
    project_id=3,
    user_id=1
  )
  revopoint_comment3 = Comment(
    comment="I already regret not ordering the turntable/premium kit in my early bird special, is there a way to order that turn table separately after launch?",
    project_id=3,
    user_id=4
  )
  revopoint_comment4 = Comment(
    comment="Perhaps ask them to add them as add ons on the campaign?",
    project_id=1,
    user_id=5
  )
  faerie_comment1 = Comment(
    comment='Congrats on a quick start and the "Project We Love" recognition. This project looks very cool and I wish you the best! - Lyn',
    project_id=4,
    user_id=1
  )
  faerie_comment2 = Comment(
    comment="It's off to a wonderful start",
    project_id=4,
    user_id=2
  )
  faerie_comment3 = Comment(
    comment="Great story",
    project_id=4,
    user_id=3
  )
  mika_comment1 = Comment(
    comment="Is this game being optimised for steam deck too?",
    project_id=5,
    user_id=5
  )
  mika_comment2 = Comment(
    comment="So if I’ve ordered the NINTENDO SWITCH COLLECTORS EDITION, does that include all 12 tarot cards or just the 4?",
    project_id=5,
    user_id=1
  )
  mika_comment3 = Comment(
    comment="I was hoping a physical edition would be made, thanks! I'm glad to be able to help and get the edition I am looking foward to!",
    project_id=5,
    user_id=2
  )
  mika_comment4 = Comment(
    comment="I was hoping a physical edition would be made, thanks! I'm glad to be able to help and get the edition I am looking foward to!",
    project_id=5,
    user_id=5
  )
  mika_comment5 = Comment(
    comment="Only 10k to go guys, what stretch goals would you want past 100k?",
    project_id=5,
    user_id=3
  )

  db.session.add(ascension_comment1)
  db.session.add(ascension_comment2)
  db.session.add(ascension_comment3)
  db.session.add(ascension_comment4)
  db.session.add(make_100_comment1)
  db.session.add(make_100_comment2)
  db.session.add(make_100_comment3)
  db.session.add(revopoint_comment1)
  db.session.add(revopoint_comment2)
  db.session.add(revopoint_comment3)
  db.session.add(revopoint_comment4)
  db.session.add(faerie_comment1)
  db.session.add(faerie_comment2)
  db.session.add(faerie_comment3)
  db.session.add(mika_comment1)
  db.session.add(mika_comment2)
  db.session.add(mika_comment3)
  db.session.add(mika_comment4)
  db.session.add(mika_comment5)
  db.session.commit()

def undo_comments():
  if environment == "production":
    db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
  else:
    db.session.execute("DELETE FROM comments")

  db.session.commit()
