from app.models import db, Pledge, db, environment, SCHEMA


def seed_pledges():
  ascention_tactics_pledges1 = Pledge(
    pledge_name="Initiate",
    price=2,
    ships_to="Anywhere in the world",
    rewards="No rewards, but receive project updates, help bring Tactics to life, and gain access to the pledge manager which includes these awesome products and many other great Stone Blade games & accessories!",
    estimated_delivery="2024-04-30",
    project_id=1,
    owner_id=1
  )
  ascention_tactics_pledges2 = Pledge(
    pledge_name="Tactics: Inferno",
    price=60,
    ships_to="Anywhere in the world",
    rewards="Get a copy of Ascension Tactics: Inferno with standees, including all non-mini stretch goals. This pledge level does not include minis.",
    estimated_delivery="2024-04-30",
    project_id=1,
    owner_id=1
  )
  ascention_tactics_pledges3 = Pledge(
    pledge_name="Full Blaze",
    price=135,
    ships_to="Anywhere in the world",
    rewards="Get Ascension Tactics: Inferno, the minis, all stretch goals, plus 3 packs of sleeves (enough for the whole game) and a playmat!",
    estimated_delivery="2024-04-30",
    project_id=1,
    owner_id=1
  )
  ascention_tactics_pledges4 = Pledge(
    pledge_name="Tactics: Inferno Experience",
    price=175,
    ships_to="Anywhere in the world",
    rewards="Get a copy of Ascension Tactics: Inferno plus the minis and all stretch goals!",
    estimated_delivery="2024-04-30",
    project_id=1,
    owner_id=1
  )
  ascention_tactics_pledges5 = Pledge(
    pledge_name="Personal Inferno",
    price=350,
    ships_to="Anywhere in the world",
    rewards="Get Ascension Tactics: Inferno and its minis, Ascension Tactics retail edition and its minis, 7 packs of sleeves (enough for both games), 2 playmats, and all stretch goals!",
    estimated_delivery="2024-04-30",
    project_id=1,
    owner_id=1
  )
  ascention_tactics_pledges6 = Pledge(
    pledge_name="Full Tactical Assault",
    price=2000,
    ships_to="Anywhere in the world",
    rewards="Get everything from the Full Blase pledge level PLUS your own hero or construct! We'll create art based on your concept and include it in all Ascension Tactics: Inferno games.",
    estimated_delivery="2024-04-30",
    project_id=1,
    owner_id=1
  )
  ascention_tactics_pledges7 = Pledge(
    pledge_name="Personal Inferno 3D",
    price=7500,
    ships_to="Anywhere in the world",
    rewards="Get everything from the Full Blase pledge level PLUS your own custom center deck champion! We'll create art and a mini sculpt based on your character design and include it in this or a future Tactics game!",
    estimated_delivery="2024-04-30",
    project_id=1,
    owner_id=1
  )
  make_100_1 = Pledge(
    pledge_name="Secret Keepers",
    price=1,
    ships_to="Only certain countries",
    rewards="As a secret keeper of the Unforgotten you have my sincerest gratitude",
    estimated_delivery="2023-05-31",
    project_id=2,
    owner_id=2
  )
  make_100_2 = Pledge(
    pledge_name="Unforgotten - Faeries",
    price=25,
    ships_to="Only certain countries",
    rewards='You will be a "Keeper" of: One Handmade, One-of a-Kind Faerie Pendant!',
    estimated_delivery="2023-05-31",
    project_id=2,
    owner_id=2
  )
  make_100_3 = Pledge(
    pledge_name="Unforgotten - Creatures",
    price=25,
    ships_to="Only certain countries",
    rewards='You will be a "Keeper" of:One Handmade, One-of a-Kind Fantasy Creature Pendant!',
    estimated_delivery="2023-05-31",
    project_id=2,
    owner_id=2
  )
  make_100_4 = Pledge(
    pledge_name="Unforgotten Collection - Set of 3!",
    price=75,
    ships_to="Only certain countries",
    rewards='You will be a "Keeper" of: Three Handmade One-of-a-Kind Pendants They can be worn or hung on your wall as a mini gallery! (Or a doll house.)',
    estimated_delivery="2023-05-31",
    project_id=2,
    owner_id=2
  )
  make_100_5 = Pledge(
    pledge_name="Unforgotten Collection - Set of 5!",
    price=125,
    ships_to="Only certain countries",
    rewards='You will be a "Keeper" of: Five Handmade One-of-a-Kind Pendants',
    estimated_delivery="2023-05-31",
    project_id=2,
    owner_id=2
  )
  revopoint_1 = Pledge(
    pledge_name="[KS Limited Special] RANGE Standard",
    price=474,
    ships_to="Anywhere in the world",
    rewards='Get the Revopoint RANGE Standard Package at the KS Limited Special Price US$474 - 35% OFF US$729. The shipping information will be collected after the campaign ends. Shipping starts in April, fast express within 7 days! A one-year warranty is included.',
    estimated_delivery="2023-05-31",
    project_id=3,
    owner_id=2
  )
  revopoint_2 = Pledge(
    pledge_name="[KS Special] RANGE Standard",
    price=547,
    ships_to="Anywhere in the world",
    rewards='Get the Revopoint RANGE Standard Package at the KS Special Price US$547 - 25% OFF US$729. The shipping information will be collected after the campaign ends. Shipping starts in April, fast express within 7 days! A one-year warranty is included.',
    estimated_delivery="2023-05-31",
    project_id=3,
    owner_id=2
  )
  revopoint_3 = Pledge(
    pledge_name="[KS Limited Special] RANGE Premium",
    price=779,
    ships_to="Anywhere in the world",
    rewards='Get the Revopoint RANGE Premium Package at the KS Limited Special Price US$779 - 35% OFF US$1199. The shipping information will be collected after the campaign ends. Shipping starts in April, fast express within 7 days! A one-year warranty is included.',
    estimated_delivery="2024-02-01",
    project_id=3,
    owner_id=2
  )
  revopoint_4 = Pledge(
    pledge_name="[KS Special] RANGE Premium",
    price=899,
    ships_to="Anywhere in the world",
    rewards='Get the Revopoint RANGE Premium Package at the KS Special Price US$899 - 25% OFF US$1199. The shipping information will be collected after the campaign ends. Shipping starts in April, fast express within 7 days! A one-year warranty is included.',
    estimated_delivery="2024-02-01",
    project_id=3,
    owner_id=2
  )
  revopoint_5 = Pledge(
    pledge_name="[Super Early Bird] RANGE Standard",
    price=328,
    ships_to="Anywhere in the world",
    rewards='Get the Revopoint RANGE Standard Package at the Super Early Bird Price US$328 - 55% OFF US$729. The shipping information will be collected after the campaign ends. Shipping starts in April, fast express within 7 days! A one-year warranty is included.',
    estimated_delivery="2024-02-01",
    project_id=3,
    owner_id=2
  )
  faerie_1 = Pledge(
    pledge_name="Digital Short Story",
    price=1,
    ships_to="Anywhere in the world",
    rewards='Get a taste of romantic fantasy with a digital version of the short story MISTRESS BOOTSI, plus my thanks!',
    estimated_delivery="2023-06-15",
    project_id=4,
    owner_id=5
  )
  faerie_2 = Pledge(
    pledge_name="Faerie Hearts - eBook",
    price=5,
    ships_to="Anywhere in the world",
    rewards='Get your copy months in advance of retail release, plus all digital stretch rewards we unlock!',
    estimated_delivery="2023-06-15",
    project_id=4,
    owner_id=5
  )
  faerie_3 = Pledge(
    pledge_name="Faerie Hearts & Mermaid Song - eBooks",
    price=10,
    ships_to="Anywhere in the world",
    rewards='An early copy of Faerie Hearts, plus Mermaid Song - a collection of five fairytale retellings.',
    estimated_delivery="2023-06-15",
    project_id=4,
    owner_id=5
  )
  faerie_4 = Pledge(
    pledge_name="Faerie Hearts - Paperback",
    price=25,
    ships_to="Anywhere in the world",
    rewards='Paperback edition (eBook included) of Faerie Hearts, delivered months before retail release, plus any unlocked stretch rewards. **US SHIPPING INCLUDED**',
    estimated_delivery="2023-06-15",
    project_id=4,
    owner_id=5
  )
  faerie_5 = Pledge(
    pledge_name="Romantic Fantasy Collection - eBook",
    price=35,
    ships_to="Anywhere in the world",
    rewards='A complete digital collection overflowing with fantasy romance! Includes all six Darkwood novels (Into the Darkwood contains the books Elfhame, Hawthorne, and Raine), plus Faerie Hearts and Mermaid Song.',
    estimated_delivery="2023-06-15",
    project_id=4,
    owner_id=5
  )
  mika_1 = Pledge(
    pledge_name="ASPIRANT WITCH",
    price=20,
    ships_to="Anywhere in the world",
    rewards="🐸 Mika and the Witch's Mountain - Digital Game in your platform📬 Digital Wallpaper Set",
    estimated_delivery="2023-11-10",
    project_id=5,
    owner_id=4
  )
  mika_2 = Pledge(
    pledge_name="LITTLE WITCH",
    price=25,
    ships_to="Anywhere in the world",
    rewards="🐸 Mika and the Witch's Mountain - Digital Game in your platform 👒 Kickstarter Exclusive Outfit 📙 Mika Digital Artbook✨ Digital goodies pack 📬 Digital Wallpaper Set",
    estimated_delivery="2023-11-10",
    project_id=5,
    owner_id=4
  )
  mika_3 = Pledge(
    pledge_name="NINTENDO SWITCH PHYSICAL EDITION",
    price=40,
    ships_to="Anywhere in the world",
    rewards='⭐You can also add the physical Nintendo Switch game to other rewards as an add-on',
    estimated_delivery="2023-11-10",
    project_id=5,
    owner_id=4
  )
  mika_4 = Pledge(
    pledge_name="MIKA COLOR FIGURE EDITION",
    price=60,
    ships_to="Anywhere in the world",
    rewards="🐈‍⬛ Mika color figure 4”/ 10cm PVC/Vynil🐸 Mika and the Witch's Mountain - Digital Game in your platform 👒 Kickstarter Exclusive Outfit 💌 Thank You Postcard (physical) 📙 Mika Digital Artbook ✨ Digital goodies pack 📬 Digital Wallpaper Set 😀 Your name in the credits",
    estimated_delivery="2023-11-10",
    project_id=5,
    owner_id=4
  )
  mika_5 = Pledge(
    pledge_name="MASTER WITCH",
    price=65,
    ships_to="Anywhere in the world",
    rewards="🐸 Mika and the Witch's Mountain - Digital Game in your platform ⚡️ Beta Access - Steam key extra 📢 Discord channel exclusive for backers 👒 Kickstarter Exclusive Outfit ⭐️ Exclusive broom trail VFX 📙 Mika Digital Artbook 💌 Thank You Postcard (physical) 🖌️ A4 Printed numbered (physical) 🎒 Witchy Sticker Pack (physical) ✨ Digital goodies pack 📬 Digital Wallpaper Set 😀 Your name in the credits",
    estimated_delivery="2023-11-10",
    project_id=5,
    owner_id=4
  )
  mika_6 = Pledge(
    pledge_name="FIGURE + NINTENDO SWITCH PHYSICAL GAME",
    price=80,
    ships_to="Anywhere in the world",
    rewards="🐈‍⬛ Mika color figure 4”/ 10cm PVC/Vynil 🎮 Mika and the Witch's Mountain - Physical Game Nintendo Switch 👒 Kickstarter Exclusive Outfit 💌 Thank You Postcard (physical) 📙 Mika Digital Artbook ✨ Digital goodies pack 📬 Digital Wallpaper Set 😀 Your name in the credits",
    estimated_delivery="2023-11-10",
    project_id=5,
    owner_id=4
  )

  db.session.add(ascention_tactics_pledges1)
  db.session.add(ascention_tactics_pledges2)
  db.session.add(ascention_tactics_pledges3)
  db.session.add(ascention_tactics_pledges4)
  db.session.add(ascention_tactics_pledges5)
  db.session.add(ascention_tactics_pledges6)
  db.session.add(ascention_tactics_pledges7)
  db.session.add(make_100_1)
  db.session.add(make_100_2)
  db.session.add(make_100_3)
  db.session.add(make_100_4)
  db.session.add(make_100_5)
  db.session.add(revopoint_1)
  db.session.add(revopoint_2)
  db.session.add(revopoint_3)
  db.session.add(revopoint_4)
  db.session.add(revopoint_5)
  db.session.add(faerie_1)
  db.session.add(faerie_2)
  db.session.add(faerie_3)
  db.session.add(faerie_4)
  db.session.add(faerie_5)
  db.session.add(mika_1)
  db.session.add(mika_2)
  db.session.add(mika_3)
  db.session.add(mika_4)
  db.session.add(mika_5)
  db.session.add(mika_6)
  db.session.commit()

def undo_pledges():
  if environment == "production":
    db.session.execute(f"TRUNCATE table {SCHEMA}.pledges RESTART IDENTITY CASCADE;")
  else:
    db.session.execute("DELETE FROM pledges")

  db.session.commit()
