user_data = []
stories = {}
viewed_stories = {}

moods = {
  'shit': u'\U0001F4A9', 
  'sad': u'\U0001F613',
  'neutral': u'\U0001F610', 
  'happy': u"\U0001F600", 
  'fire': u"\U0001F525"
  }

memes = [
  'https://sayingimages.com/wp-content/uploads/dont-worry-you-got-this-motivational-memes.jpg',
  'https://i.kym-cdn.com/photos/images/original/002/256/988/755.jpg',
  'https://i.kym-cdn.com/photos/images/original/002/223/209/e5f.jpg',
  'https://bestlifeonline.com/wp-content/uploads/sites/3/2019/08/f3ljesn386h31.jpg?quality=82&strip=all',
  'https://stayhipp.com/wp-content/uploads/2018/09/FB-wholesome-memes-.jpg',
  'https://static.boredpanda.com/blog/wp-content/uploads/2019/06/8-5cff8a4c38b6d__700.jpg',
  'https://static.thehoneycombers.com/wp-content/uploads/sites/4/2020/08/funny-coronavirus-meme-2020.jpg',
  'https://www.asiaone.com/sites/default/files/styles/a1_og_image/public/original_images/Jul2021/20211507_KTVmainimage.jpg?itok=TOy3xNBN',
  'https://static.boredpanda.com/blog/wp-content/uploads/2020/05/2-5ec29bef3b74b__700.jpg',
  'https://i.redd.it/4cw0uzr8nc431.png',
  'https://memezila.com/wp-content/Well-in-that-case-meme-5741.png',
  'https://i.kym-cdn.com/photos/images/original/001/724/733/73e.jpg',
  'https://pics.me.me/thumb_these-are-for-dads-and-anyone-else-who-enjoys-a-72471534.png'
]

quotes = {
  'shit': ['https://i1.wp.com/www.dailyinspirationalquotes.in/diqmmediaupld/2016/11/pexels-photo-29521-min.jpg?w=750&ssl=1',
  'https://cdn.powerofpositivity.com/wp-content/uploads/2020/08/Each-day-you-only-have-a-limited-amount-of-time-and-energy.-Dont-waste-it-stressing-about-things-you-cannot-control..png',
  'https://putthekettleon.ca/wp-content/uploads/2017/10/Even-the-darkest-night-will-end-and-the-sun-will-rise.-683x1024.jpg',
  'https://www.yourtango.com/sites/default/files/styles/header_slider/public/image_blog/feeling-down-quotes.jpg?itok=4nEyqMBB',
  'https://www.quoteambition.com/wp-content/uploads/2017/03/cant-control-let-go.jpg?ezimgfmt=rs:380x380/rscb1/ng:webp/ngcb1'],

  'sad': ['https://www.healthyplace.com/sites/default/files/2020-04/sad-life-quotes.jpg',
    'https://lovsms.com/wp-content/uploads/2021/05/Sad-Quotes1.jpg',
    'https://www.keepinspiring.me/wp-content/uploads/2021/06/sad-is-a-health-feeling-jk-rowling-quote.png',
    ],

    'neutral':['https://data.whicdn.com/images/330885800/original.jpg',
    'https://marketplace.canva.com/EAEQyjLSIrs/1/0/1131w/canva-quote-poster-you-will-never-have-this-day-again-so-make-it-count.-neutral-beige-and-orange-colors-JTrIr6ppJIw.jpg',
    'https://i.pinimg.com/originals/76/c7/9e/76c79e4c16654d6ba22f683841bb04f1.jpg',
    'https://marketplace.canva.com/EAEl_RinTGA/1/0/900w/canva-neutral-abstract-motivational-quote-phone-wallpaper-sPG5OXvLjMg.jpg',
    'https://i.pinimg.com/originals/fc/aa/c2/fcaac2cc3d9d42fb48681b09e21f4f0b.png',
    'https://marketplace.canva.com/EAErc44028w/2/0/1131w/canva-beige-neutral-simple-minimalist-chic-aesthetic-elegant-wisdom-motivational-quote-good-vibes-poster-print-7gX9FLeplSE.jpg'
    ],

    'happy' : ['https://www.coolfunnyquotes.com/images/quotes/680/an-apple-a-day-keeps-anyone-away.jpg',
    'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gh-happiness-quotes-23-mother-teresa-1621886511.png',
    'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gh-happiness-quotes-14-lilly-pulitzer-1621885979.png?crop=1xw:1xh;center,top&resize=480:*',
    'https://statussayings.com/wp-content/uploads/2016/09/Happiness-quotes.png',
    'https://i.pinimg.com/736x/d1/43/1a/d1431a494c17209037c74489f091fd75.jpg'
    ],

  'fire': 
    ['https://wisdomquotes.b-cdn.net/wp-content/uploads/anger-quotes-if-you-hate-a-person-then-you-are-defeated-by-them-confucius-wisdom-quotes.jpg',
    'https://i.pinimg.com/564x/dd/71/b7/dd71b7aa20313f9d86846d597e7e1bfe--anger-quotes-control-quotes-anger.jpg',
    'https://i2.wp.com/www.dailyinspirationalquotes.in/diqmmediaupld/2018/12/man_rep201220185-min.jpg?resize=696%2C1044&ssl=1',
    'https://cdn.powerofpositivity.com/wp-content/uploads/2020/11/be-selective-battles-300x300.jpeg',
    'https://i.pinimg.com/originals/f9/6d/3d/f96d3d36398aa42935329b8ca9fd003c.jpg']
  
}

