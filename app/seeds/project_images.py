from app.models import db, ProjectImages, environment, SCHEMA


def seed_project_images():
  ascension_images1 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/032/180/f0af89a023186dad2106b58bbb37f9e5_original.jpg?ixlib=rb-4.0.2&crop=faces&w=352&h=198&fit=crop&v=1677108419&auto=format&frame=1&q=92&s=2f091a8f001b9265249f1f88ca1a40aa",
    project_id=1
  )
  ascension_images2 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/881/868/5533b000ac0761b92dfe81b327c5427c_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1675776795&gif-q=50&q=92&s=9feee17dd5b539f1cb48e7aab545579f",
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
    url="https://ksr-ugc.imgix.net/assets/040/078/618/2628ec261096ceb56d281ee971531f2f_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1677538354&gif-q=50&q=92&s=3e071f0cb3fae4834a63dac11b15c02f",
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
  mika_images1 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/055/776/ef963df0887a5574faa5578eea5fe5ad_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1677315479&gif-q=50&lossless=true&s=aec6351a41b910dd34764ed1c485d510",
    project_id=5
  )
  mika_images2 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/098/867/b56d4fe4341cdcdb34b7582fcbbc5e30_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1677686032&gif-q=50&lossless=true&s=38d68432d4acf4f29834975f0d7416d8",
    project_id=5
  )
  mika_images3 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/062/906/8860ab7f63386c7b293364482abfa4cf_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1677402339&gif-q=50&lossless=true&s=62d05b3838d1ec4630647a663d45b503",
    project_id=5
  )
  mika_images4 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/915/001/cfc035858eea6c5c97a8784b292bf0b7_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1676045132&gif-q=50&lossless=true&s=133080d823c59826e16f0935f3d758e1",
    project_id=5
  )
  mika_images5 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/098/887/e5b7645cf3207af0a58dd2b0a595e4ad_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1677686173&gif-q=50&lossless=true&s=33802e238270e5b19e35a62bd07568ec",
    project_id=5
  )
  mika_images6 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/577/123/b25b682b6d0d8d0b11ba9972d609a8fb_original.gif?ixlib=rb-4.0.2&w=680&fit=max&v=1672736769&gif-q=50&q=92&s=136be9038b15ffe240d1d71cc23d762d",
    project_id=5
  )
  mika_images7 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/455/434/0b80aa78fb445aebf96e3306676c95a8_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1670949040&gif-q=50&lossless=true&s=b72c44d35c7adbc57ceabe3ede678351",
    project_id=5
  )
  good_day_images1 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/727/766/4989cc7b5477266355ddcbcecd3d760a_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1674321118&gif-q=50&lossless=true&s=e3ba3974d7e696494b28b8a8ce52eff7",
    project_id=6
  )
  good_day_images2 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/727/755/712dc509975988e1072dd2dc7794b6e2_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1674321034&gif-q=50&lossless=true&s=9d2d96e99491b254bfd4a5c38790ba7f",
    project_id=6
  )
  good_day_images3 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/732/321/b981cb1f2b60c5b34c13c1b80a566ed5_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1674391907&gif-q=50&q=92&s=cec27130d122bdde92137320f6348c99",
    project_id=6
  )
  good_day_images4 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/732/322/7b92b9d2f18202ecb9b968260ba2d637_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1674391969&gif-q=50&q=92&s=11ac30ad39564417676d84bae018074e",
    project_id=6
  )
  watch_images1 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/962/946/c2d7164a1dfd6cda8bf98b5c096c726c_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1676495072&gif-q=50&q=92&s=67779e7595c1266cbc5d0ac1e5f99208",
    project_id=7
  )
  watch_images2 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/962/863/cb03aa12cdfe91bfb701830cf57539af_original.gif?ixlib=rb-4.0.2&w=680&fit=max&v=1676494664&gif-q=50&q=92&s=3a385a82a640d9adddb6d3d45958b928",
    project_id=7
  )
  watch_images3 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/908/550/9b0f876cd24fa1d83b15566c23a1bd53_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1675987108&gif-q=50&q=92&s=788671ad61d525abf3e3f364ad5b99b8",
    project_id=7
  )
  watch_images4 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/053/120/5c4318e4edd940f4c28c0243b9224f95_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1677280090&gif-q=50&q=92&s=65cb6d545a04465f94514ae01939c8f0",
    project_id=7
  )
  dogs_images1 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/007/816/22d89c5554211acc9777ba054d4aaad3_original.jpg?ixlib=rb-4.0.2&crop=faces&w=1024&h=576&fit=crop&v=1676930580&auto=format&frame=1&q=92&s=994ab30bb29de52300cbaf7da16112f2",
    project_id=8
  )
  dogs_images2 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/005/623/fcaa24d8a52882fbfe4d8d945bc046e7_original.gif?ixlib=rb-4.0.2&w=680&fit=max&v=1676916448&gif-q=50&q=92&s=aef45789b800f856f21cee300506924d",
    project_id=8
  )
  dogs_images3 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/005/895/1fa07607921dd3b0739ced23799f0361_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1676918027&gif-q=50&lossless=true&s=5787884c416fc6babc2e7070a89d666b",
    project_id=8
  )
  dogs_images4 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/006/078/1de9f643be5385ab473168043ea5c75e_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1676919101&gif-q=50&lossless=true&s=cd9d435c7989612df790e47439e5f823",
    project_id=8
  )
  dogs_images5 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/007/151/ff5139d9c27b2dbdaae1b4cab43078ac_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1676926523&gif-q=50&q=92&s=53d7670d8306e17fa0df77e34eb0b11e",
    project_id=8
  )
  dogs_images6 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/008/647/a7c92478a124259e25407e51237471a9_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1676936373&gif-q=50&q=92&s=7e308f9f3d68daee290d4dee4d2dbae3",
    project_id=8
  )
  soul_images1 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/759/347/bd24bcaaea3cccfa99e7056e87150634_original.gif?ixlib=rb-4.0.2&w=680&fit=max&v=1674649590&gif-q=50&q=92&s=1dd05d1f73ad51115f2dcc13c4c05d40",
    project_id=9
  )
  soul_images2 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/040/094/407/4267af6e50faad522877718885298f9c_original.png?ixlib=rb-4.0.2&w=680&fit=max&v=1677651922&gif-q=50&lossless=true&s=3f62bd9fdee5ca137d4cee3df97dd72d",
    project_id=9
  )
  soul_images3 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/885/629/0c38e591298c7464b5843e1ae637f18f_original.gif?ixlib=rb-4.0.2&w=680&fit=max&v=1675797489&gif-q=50&q=92&s=41833e00b0f449a66f36a8b7b96a88a5",
    project_id=9
  )
  soul_images4 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/742/594/dca31d1df8b8194c896f602ec81e6dd6_original.jpg?ixlib=rb-4.0.2&w=680&fit=max&v=1674499456&gif-q=50&q=92&s=9bc98d7eb6b68fbed0df5ddd0e620590",
    project_id=9
  )
  soul_images5 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/673/566/b4a10e7690fc866be68a555ad184a3e3_original.gif?ixlib=rb-4.0.2&w=680&fit=max&v=1673790443&gif-q=50&q=92&s=3c6795a5c393c29ab5e9fc68ec72b193",
    project_id=9
  )
  soul_images6 = ProjectImages(
    url="https://ksr-ugc.imgix.net/assets/039/644/833/ecf45339cad09e8a58ee64011636a7bd_original.gif?ixlib=rb-4.0.2&w=680&fit=max&v=1673459202&gif-q=50&q=92&s=4656cffdb9374f0e244c002916dc7103",
    project_id=9
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
  db.session.add(mika_images1)
  db.session.add(mika_images2)
  db.session.add(mika_images3)
  db.session.add(mika_images4)
  db.session.add(mika_images5)
  db.session.add(mika_images6)
  db.session.add(mika_images7)
  db.session.add(good_day_images1)
  db.session.add(good_day_images2)
  db.session.add(good_day_images3)
  db.session.add(good_day_images4)
  db.session.add(watch_images1)
  db.session.add(watch_images2)
  db.session.add(watch_images3)
  db.session.add(watch_images4)
  db.session.add(dogs_images1)
  db.session.add(dogs_images2)
  db.session.add(dogs_images3)
  db.session.add(dogs_images4)
  db.session.add(dogs_images5)
  db.session.add(dogs_images6)
  db.session.add(soul_images1)
  db.session.add(soul_images2)
  db.session.add(soul_images3)
  db.session.add(soul_images4)
  db.session.add(soul_images5)
  db.session.add(soul_images6)
  db.session.commit()

def undo_project_images():
  if environment == "production":
    db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
  else:
    db.session.execute("DELETE FROM projectImages")

  db.session.commit()
