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
  revopoint_images1 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/819/481/d2b72c52d01df3d39b169e7c7aff3560_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1675217053&gif-q=50&q=92&s=9c7287d3721d924709e8887335ba94eb",
    project_id=3
  )
  revopoint_images2 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/879/120/b94be72eb3462178b5181cd790c823e7_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1675753901&gif-q=50&q=92&s=88d10cb85ef24acdf06ed1e233635f75",
    project_id=3
  )
  revopoint_images3 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/878/962/fddd21664e9dc6f7a542bf2bf86c2a72_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1675752514&gif-q=50&q=92&s=013aad11c97b28536d9231b705515b43",
    project_id=3
  )
  revopoint_images4 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/032/902/80d7ffa2cca20d7a5084755c1d3a5a7c_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1677116011&gif-q=50&q=92&s=b9f87764d87e04e3c127930b6eb165c5",
    project_id=3
  )
  revopoint_images5 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/032/902/80d7ffa2cca20d7a5084755c1d3a5a7c_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1677116011&gif-q=50&q=92&s=b9f87764d87e04e3c127930b6eb165c5",
    project_id=3
  )
  revopoint_images6 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/879/241/f3dc7f706ad48437def639e5ec342061_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1675754823&gif-q=50&q=92&s=42d6f1872fd4d48d5a3e49f48ea94bf6",
    project_id=3
  )
  revopoint_images7 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/978/177/ee039393ce8563a75505654ae79b374c_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1676619072&gif-q=50&q=92&s=767814d2e15261846e8837abe24dc8d7",
    project_id=3
  )
  revopoint_images8 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/879/245/96e9dea5a6405ce15b7fce3421c94f98_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1675754848&gif-q=50&q=92&s=27d1dcc760b2fb4ad28fe6ea8d6f7ed8",
    project_id=3
  )
  revopoint_images9 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/842/256/764a5eb0e054b8f97a9aafb87cbe07c7_original.gif?ixlib=rb-4.0.2&w=680&fit=max&v=1675407367&gif-q=50&q=92&s=033cf20a15f0872571478e37c8b14ba9",
    project_id=3
  )
  revopoint_images10 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/842/261/3afeee0568962e0ec365be15055a9da2_original.gif?ixlib=rb-4.0.2&w=680&fit=max&v=1675407417&gif-q=50&q=92&s=0479fe026a0aad54041404a7e559dead",
    project_id=3
  )
  faerie_images1 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/821/388/4f254490d28cd611a87b96f02ce8aca8_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1675234874&gif-q=50&lossless=true&s=5f59aa137b26eae3a8511ad7e896f4aa",
    project_id=4
  )
  faerie_images2 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/717/697/dcf2b9e3ad727319f7955038ce0113d0_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1674200129&gif-q=50&lossless=true&s=db9373b7f8dbd9689dffa57f4b808d5b",
    project_id=4
  )
  faerie_images3 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/717/715/fb0ec580c2ad17da5018c581cf23509b_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1674200510&gif-q=50&lossless=true&s=c1f08b1f13a3d1b04d7b6e010b794cdc",
    project_id=4
  )
  faerie_images4 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/725/804/6483d21da8bd940630dc31f459811f2c_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1674291347&gif-q=50&lossless=true&s=4d97d2bfbb406722331113a29377f1e2",
    project_id=4
  )
  faerie_images5 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/950/713/738e60597e3b712d7ecad89c03917c29_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1676399922&gif-q=50&lossless=true&s=e5ebd296e2a099ca37b8041b9863dbd1",
    project_id=4
  )
  faerie_images6 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/879/051/866602c68bf4fd55c66c47e4f2278b1d_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1675753292&gif-q=50&lossless=true&s=1c0a65d18db849ae5f069a5543e9f82c",
    project_id=4
  )
  faerie_images7 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/821/415/9c441ebbd5b8edd7c5f239bf4665f06d_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1675235274&gif-q=50&lossless=true&s=cce905d6a82562243a1b10aab629266c",
    project_id=4
  )
  faerie_images8 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/616/509/48bf7d10ca1eceba59c090e34613217a_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1673164170&gif-q=50&lossless=true&s=810e91d91af9815eee68ac453a4caf21",
    project_id=4
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
  db.session.add(make_100_images1)
  db.session.add(make_100_images2)
  db.session.add(make_100_images3)
  db.session.add(make_100_images4)
  db.session.add(make_100_images5)
  db.session.add(make_100_images6)
  db.session.add(revopoint_images1)
  db.session.add(revopoint_images2)
  db.session.add(revopoint_images3)
  db.session.add(revopoint_images4)
  db.session.add(revopoint_images5)
  db.session.add(revopoint_images6)
  db.session.add(revopoint_images7)
  db.session.add(revopoint_images8)
  db.session.add(revopoint_images9)
  db.session.add(revopoint_images10)
  db.session.add(faerie_images1)
  db.session.add(faerie_images2)
  db.session.add(faerie_images3)
  db.session.add(faerie_images4)
  db.session.add(faerie_images5)
  db.session.add(faerie_images6)
  db.session.add(faerie_images7)
  db.session.add(faerie_images8)
  db.session.commit()

def undo_project_images():
  if environment == "production":
    db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
  else:
    db.session.execute("DELETE FROM projectImages")

  db.session.commit()
