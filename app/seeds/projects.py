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
    end_day="2023-08-23",
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
    end_day="2023-07-20",
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
    end_day="2024-05-13",
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
    end_day="2023-10-16",
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
    end_day="2024-01-22",
    project_type="game",
    owner_id=4
  )
  good_day = Project(
    project_name="'Good Day': a darkly comic new play about AI & immortality",
    description="Help us bring 'Good Day' to Vault Festival in London this March.",
    story="""
      Double Telling (Instagram | Twitter) is a theatre company dedicated to developing bold new plays for the stage. 
      Led by director & dramaturg Marlie Haco, we make experimental shows that seek to engage audiences in provocative ways. 
      Our last show Proud played for an extended run at the King’s Head Theatre in 2022 and received 5-star reviews.  
    """,
    risks="""
      Making live theatre involves team-related risks, including actors getting unwell or injured, but 'the show will go on' unless 
      there is a major incident affecting the team such as a serious illness where a replacement cannot be found in time, or the Vault 
      Festival itself is cancelled due to external unforeseeable events.
    """,
    goal=6000,
    current_fund=0,
    backers=0,
    end_day="2023-08-02",
    project_type="art",
    owner_id=6
  )
  watch = Project(
    project_name="An Innovative Wandering Hour Watch | Vendetta II Automatic",
    description="Our upgrades to the original Vendetta make the unattainable attainable, bringing a sub-$1000 wandering hour watch to everyone.",
    story="""
      Xeric was started from a passion to push the boundaries of design and create unique, yet affordable time machines. 
      Watches like you've never seen before. We’ve launched and fulfilled over 17 fully-funded projects since the beginning, 
      including the most successful wristwatch campaign in the history of Kickstarter at $5.4 million. We deliver on our promises.
    """,
    risks="""
      COVID-19 could impact production if there's a surge in cases at our factories or in Hong Kong which could cause the border to be 
      closed and reduction in freight flights coming in and out of Hong Kong. Our backers will be in the loop as we communicate updates at every stage of the process.
    """,
    goal=10000,
    current_fund=0,
    backers=0,
    end_day="2024-02-02",
    project_type="design",
    owner_id=4
  )
  dogs = Project(
    project_name="MAD DOGS: VOLUME 1",
    description='Cyberpunk LGBT+ crime story by the author of "Paper Roses" webcomic.',
    story="""
      A cyberpunk crime story with a sprinkle of rock (the music, not stone) and fully LGBT+ main cast. Ranked +18 for explicit language, violence and adult content in future volumes
    """,
    risks="""
      Every aspect of physical rewards have been tested and perfected before the launch to be sure everything is absolutely 100%/ ready to order once the campain ends. 
      The biggest challenge then will be the shipping alone. I have an experience with shipping big amounts of orders thanks to my online store, but my friends warned me 
      Kickstarter orders may get overwhelming in numbers compared to a regular store opening. I will pack it all with my friend so there will be only two of us vs. (probably) 
      a LOT of books so please be patient with us!
    """,
    goal=10000,
    current_fund=0,
    backers=0,
    end_day="2023-09-10",
    project_type="publishing",
    owner_id=7
  )
  soul = Project(
    project_name="Soul Passage - Hand drawn 2D action Metroidvania",
    description='Travel through different worlds to save your family! Fight, solve, craft, travel, explore, and progress! DO IT AGAIN,',
    story="""
      Soul Passage is an action-packed 2D hand-drawn Metroidvania game that offers a unique experience for players. With features such as Fast-paced combat, 
      solving puzzles, crafting, travelling, exploring, and progression, this game breaks the mould of traditional Metroidvania titles. 
      Players are given control of the skill tree and the fate of the main character, Obligor, as they embark on an extraordinary journey through the Soul Passage, 
      a soul realm filled with diverse planets, creatures, and an abundance of magical items and weapons to discover.
    """,
    risks="""
      Soul Passage is a game brought to you by a passionate developer with a background in the game industry. 
      Emrah Özbay, who handles art direction and implementation, has been working tirelessly to create the best game possible given the limitations. 
      My goal is to bring together my passions and experiences to create a game that will not disappoint.
    """,
    goal=33884,
    current_fund=0,
    backers=0,
    end_day="2023-09-01",
    project_type="game",
    owner_id=8
  )

  db.session.add(ascension_tactics)
  db.session.add(make_100)
  db.session.add(revopoint)
  db.session.add(faerie)
  db.session.add(mika)
  db.session.add(good_day)
  db.session.add(watch)
  db.session.add(dogs)
  db.session.add(soul)
  db.session.commit()


def undo_projects():
  if environment == "production":
    db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
  else:
    db.session.execute("DELETE FROM projects")

  db.session.commit()
