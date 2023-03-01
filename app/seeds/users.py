from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', 
        email='demo@aa.io', 
        password='password',
        first_name='Demo',
        last_name='Lition',
        bio='Our vision is to build the right products that let people explore the natural world without limits.',
        profile_image='https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1180&q=80'
    )
    marnie = User(
        username='marnie', 
        email='marnie@aa.io', 
        password='password',
        first_name='Marnie',
        last_name='Wan',
        bio='We create thoughtful accessories for your favorite RPGs & board games, and expertly crafted furniture to redefine and elevate your tabletop gaming experience.',
        profile_image='https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80'
    )
    bobbie = User(
        username='bobbie', 
        email='bobbie@aa.io', 
        password='password',
        first_name='Bobbie',
        last_name='Toa',
        bio='The company was formed in 2012 to take advantage of our experience in gaming, bringing both classic titles - many of which defined entire genres - and new exciting games to PC, Mac and various mobile devices.',
        profile_image='https://img.freepik.com/premium-vector/board-game-logo-design_705304-22.jpg?w=2000'
    )
    ned = User(
        username='nedned', 
        email='ned@aa.io', 
        password='password',
        first_name='Ned',
        last_name='Ned',
        bio="We're publishing a weekly series of video interviews with Black creators who have run successful Kickstarter campaigns across various creative fields. Plus: new TCI interviews, live projects, and more.",
        profile_image='https://steamuserimages-a.akamaihd.net/ugc/1644340994747007967/853B20CD7694F5CF40E83AAC670572A3FE1E3D35/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true'
    )
    emily = User(
        username='emily', 
        email='emily@aa.io', 
        password='password',
        first_name='Emily',
        last_name='Vu',
        bio='I launched RollvsEvil a not-for-profit charitable fundraising effort for the tabletop community to combat real-world evils starting with frontline humanitarian aid support for the people of Ukraine.',
        profile_image='https://wallpaperaccess.com/full/82955.jpg'
    )
    toby = User(
        username='toby', 
        email='toby@aa.io', 
        password='password',
        first_name='Toby',
        last_name='Mather',
        bio='Startup founder by day, theatre photographer and producer by night',
        profile_image='https://ksr-ugc.imgix.net/assets/010/621/542/1b75a69e642dcffb8fe4557b5b25d2c8_original.jpg?ixlib=rb-4.0.2&w=160&h=160&fit=crop&v=1674424003&auto=format&frame=1&q=92&s=1d92eb81a2b7e060e7bce1ca0dcc838c'
    )
    mathew = User(
        username='mathew', 
        email='mathew@aa.io', 
        password='password',
        first_name='Mathew',
        last_name='Brand',
        bio='Game lover',
        profile_image='https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yasuo_0.jpg'
    )
    david = User(
        username='david', 
        email='david@aa.io', 
        password='password',
        first_name='David',
        last_name='Dhr',
        bio='Best cohort lead ever',
        profile_image='https://static.wikia.nocookie.net/kirby/images/c/c6/Kirby_RtDDX.png/revision/latest?cb=20230127153557&path-prefix=en'
    )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(ned)
    db.session.add(emily)
    db.session.add(toby)
    db.session.add(mathew)
    db.session.add(david)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")
        
    db.session.commit()
