from app.models import db, ProjectImages, environment, SCHEMA


def seed_project_images():
  ascension_images1 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/017/318/b1499e87616d1a7f4dc0c9ff573caad4_original.jpg?ixlib=rb-4.0.2&crop=faces&w=352&h=198&fit=crop&v=1677000209&auto=format&frame=1&q=92&s=24da4fc981e20491ba3ed33e2f6a8904",
    project_id=1
  )
  ascension_images2 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/004/718/3878d6e69b71fe5651f60536156a9049_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1676911247&gif-q=50&q=92&s=f34e0bd48f43809c07d54c697286f36f",
    project_id=1
  )
  ascension_images3 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/004/381/82c631857fc5f238c97eeb5908d68eef_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1676909036&gif-q=50&q=92&s=4774377ba8c35a2daf2190a479b23e90",
    project_id=1
  )
  ascension_images4 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/013/724/bc2ac9566e8cfd3184408f129a9ce92f_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1676978738&gif-q=50&q=92&s=3abe136e267e874fb52a4e6ce8c573d0",
    project_id=1
  )
  ascension_images5 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/013/724/bc2ac9566e8cfd3184408f129a9ce92f_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1676978738&gif-q=50&q=92&s=3abe136e267e874fb52a4e6ce8c573d0",
    project_id=1
  )
  ascension_images6 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/017/367/d2149c7ac3831032734d25ca029ff40d_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1677000426&gif-q=50&q=92&s=fbdd04c824792b3c41319e2fb1717c49",
    project_id=1
  )
  ascension_images7 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/012/065/ee5fd629590c73965951774917f3c4a4_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1676965083&gif-q=50&q=92&s=4f3c07fa6a2d38131dfd5362933fbbbf",
    project_id=1
  )
  ascension_images8 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/003/869/f0fb8c6a54ca96e5098c6453edcf8a13_original.gif?ixlib=rb-4.0.2&w=680&fit=max&v=1676905870&gif-q=50&q=92&s=ea0334996132f24f1ee7a01d74605b2f",
    project_id=1
  )
  ascension_images9 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/003/875/4410b05d123e9b0195cfd2b4540dd21d_original.gif?ixlib=rb-4.0.2&w=680&fit=max&v=1676905910&gif-q=50&q=92&s=466c7ba0c196c323cc39bad7e7868ade",
    project_id=1
  )
  ascension_images10 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/017/743/94b17b66c770d59382ae9778072e689c_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1677002423&gif-q=50&q=92&s=983a40a3aef1b2f4191f831d65dcaaf0",
    project_id=1
  )
  make_100_images1 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/790/285/da7097c2e9ae59de360bcc4afcd4fbdf_original.jpg?ixlib=rb-4.0.2&crop=faces&w=1024&h=576&fit=crop&v=1674955749&auto=format&frame=1&q=92&s=d85759bcf058c98f6f0c90224fee62fe",
    project_id=2
  )
  make_100_images2 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/790/875/827f7a12d9224958e0751ec4331e1a31_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1674963303&gif-q=50&q=92&s=2485389c9370c262c132359a596c6441",
    project_id=2
  )
  make_100_images3 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/790/213/6c6cc00a60a11df27966b8494df7e01f_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1674954757&gif-q=50&q=92&s=b786f7a7d6a37fc582b6a5d2e9b70b14",
    project_id=2
  )
  make_100_images4 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/790/220/ea04ba9b4b6d21071cd8d87833aaa6d6_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1674954903&gif-q=50&q=92&s=5c1b66391e302246fc66605a581f9989",
    project_id=2
  )
  make_100_images5 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/790/233/1758985b67f83dffed0b2600e029924a_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1674955088&gif-q=50&q=92&s=b96ee134c29828bf443bfe34a3732cb3",
    project_id=2
  )
  make_100_images6 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/764/512/fcb74ed4ad26ecd926dfc868d04fc7de_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1674687674&gif-q=50&q=92&s=d6da6eae17faf11d86ae7aedbb19c16d",
    project_id=2
  )
  
  db.session.add(ascension_images1)
  db.session.add(ascension_images2)
  db.session.add(ascension_images3)
  db.session.add(ascension_images4)
  db.session.add(ascension_images5)
  db.session.add(ascension_images6)
  db.session.add(ascension_images7)
  db.session.add(ascension_images8)
  db.session.add(ascension_images9)
  db.session.add(ascension_images10)
  db.session.add(make_100_images1)
  db.session.add(make_100_images2)
  db.session.add(make_100_images3)
  db.session.add(make_100_images4)
  db.session.add(make_100_images5)
  db.session.add(make_100_images6)
  db.session.commit()

def undo_project_images():
  if environment == "production":
    db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
  else:
    db.session.execute("DELETE FROM projectImages")

  db.session.commit()
