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
    end_day="2023-03-23",
    project_type="game",
    owner_id=1
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
    end_day="2023-04-20",
    project_type="art",
    owner_id=2
  )
  revopoint = Project(
    project_name='Revopoint RANGE: Big Scans, Big Detail',
    description="An Affordable and Accurate Big Object Infrared Structured Light 3D Scanner.",
    story="""
      We're back and ready to introduce our brand new Revopoint RANGE, the world's first affordable 
      large objects scanner with a single capture range of 360mm x 650 mm@600mm. As many of you already know, 
      Revopoint is no stranger to Kickstarters. With over 17,000 backers and more than $8.2 million raised 
      from three successful Kickstarter campaigns for the POP, POP 2, and MINI 3D Scanners.
    """,
    risks="""
    We are more than confident that we can deliver the Revopoint RANGE as the design and 
    engineering work are finished, and we have already extensively tested it. Furthermore, 
    we have successfully run three previous Kickstarter projects, and our manufacturing and 
    supply capacity has expanded and matured over these projects. In other words, aside from any logistical challenges that might arise and 
    which we commit to solving promptly, we do not see any risk on the project’s horizon.
    """,
    goal=10000,
    current_fund=0,
    backers=0,
    end_day="2023-05-13",
    project_type="design",
    owner_id=2
  )
  faerie = Project(
    project_name='Faerie Hearts: A Romantic Fantasy Collection',
    description="Tales of love and adventure set in worlds ranging from Ancient Celtic moors to an enchanted forest, where romance and magic reign.",
    story="""
      Magical happily-ever-afters are yours in this brand new collection of sweetly romantic stories from USA Today bestselling author Anthea Sharp.
      From a heroine of Celtic legend to an intrepid elf warrior, fall in love with these couples bound by fate, who must fight for everything they 
      hold dear in order to gain their true loves.
    """,
    risks="""
    After running several Kickstarter campaigns, I've learned to build in extra time for the printing process. Things always go slower than I'd like! 
    Delays can crop up with misprinted books, too, or shipping issues, which always affect a couple people per campaign, unfortunately.Other than that, 
    I'm an experienced indie author with over 40 books under my belt, and have no worries about holding up my end of the deal!
    """,
    goal=1000,
    current_fund=0,
    backers=0,
    end_day="2023-04-16",
    project_type="publishing",
    owner_id=5
  )
  mika = Project(
    project_name="Mika and the Witch's Mountain - delivery service adventure",
    description="Soar the sky on this adventure of Mika, an aspiring witch. Deliver packages to the inhabitants from the Island of Winds.",
    story="""
      Mika and the Witch’s Mountain is a fantasy adventure about an aspiring witch who delivers packages to the townspeople of a small island. 
      Explore every nook and cranny and soar through the sky with your magic broom.
    """,
    risks="""
    We're a small group of people who have worked hard for a year to advance significantly the development of Mika and the Witch’s Mountain; 
    consequently, the game will be a reality soon and incompletion rendered an impossibility.

    Despite this, we’re professionals from different teams and areas, and even though things are going smoothly, it’s the first time we work 
    together on the same project. This can lead to very different points of view and approaches to some aspects of the game that can make the 
    development changes and may even lengthen a little more in time, which means more budget and iteration to achieve the game that we all dream about. 
    We want Mika and the Witch’s Mountain to be a good and memorable game, and for that reason, we are counting on your help in this final phase of development.
    """,
    goal=42000,
    current_fund=0,
    backers=0,
    end_day="2023-07-22",
    project_type="game",
    owner_id=4
  )

  db.session.add(ascension_tactics)
  db.session.add(make_100)
  db.session.add(revopoint)
  db.session.add(faerie)
  db.session.add(mika)
  db.session.commit()


def undo_projects():
  if environment == "production":
    db.session.execute(f"TRUNCATE table {SCHEMA}.projects RESTART IDENTITY CASCADE;")
  else:
    db.session.execute("DELETE FROM projects")

  db.session.commit()
