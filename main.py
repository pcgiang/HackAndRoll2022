import os

import telebot, schedule, random
from threading import Thread
from time import sleep

from telebot.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup

from database import user_data, stories, memes, moods, quotes, viewed_stories

#HackNRollTestBot
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

bot.set_my_commands([
  BotCommand('start','Starts the bot.'),
  BotCommand('help', 'A detailed explanation of what I can do!'),
  BotCommand('mood', 'Tell the bot about your mood!'),
  BotCommand('share', 'Tell a story to someone!'),
  BotCommand('view', 'See someone else\'s story.'),
  BotCommand('meme', 'Look at some memes to make you nose exhale.')
])

def request_start(chat_id):
  """
  Helper function to request user to execute command /start
  """
  if chat_id not in user_data:
    bot.send_message(chat_id=chat_id, text='Please start the bot by sending /start')
 
  return

@bot.message_handler(commands=['start'])
def start(message):
  """
  Command that welcomes the user and configures the initial setup
  """
  chat_id = message.chat.id

  if message.chat.type == 'private':
    chat_user = message.chat.first_name
  else:
    # not meant for groups
    chat_user = message.chat.title

  welcome_message = 'Hi ' + chat_user + '! '
  # Add a prompt to click 'help'
  welcome_message += 'Welcome to halloFriendBot!'
  welcome_message += 'Use the \"/help\" command to view the list of commands that you can use :)'

  # initialise empty list for each user
  if chat_id not in user_data:
    user_data.append(chat_id)
  bot.reply_to(message, welcome_message)

  print(user_data)
  print(stories)

@bot.message_handler(commands=['help'])
def help(message):
  """
  Command that describes various commands and features of the bot
  """
  bot.send_message(message.chat.id, 'Here is a list of available commands!\n\n\n/start: Starts the bot. You have already done this! CAUTION: Do not click this again unless you want to reset the bot.\n\n/help: Opens the help page, which you are at now!\n\n/share: Share about your day to a random user anonymously, who will be able to respond to your story anonymously as well!\n\n/view: View someone else\'s story, which you will be able to comment on! Listen to others and leave a nice response :)\n\n/meme: Have a professionally procured meme sent to you straight on telegram!')

@bot.message_handler(commands=['share'])
def share(message):
  """
  Command that allows user to share their story 
  """
  chat_id = message.chat.id
  sent = bot.send_message(chat_id, "What story would you like to share?")

  def userInput(message):
    message_text = message.text
    
    if chat_id not in stories:
      stories[chat_id] = []
      viewed_stories[chat_id] = []
    
    # add text into stories
    stories[chat_id].append(message_text)
    viewed_stories[chat_id].append(message_text)
    print(f'story by {chat_id} is added')
    bot.reply_to(message, "Thank you for sharing your story!")
    for user in stories:
      print(stories[user])
    return

  bot.register_next_step_handler(sent, userInput)

@bot.message_handler(commands=['view'])
def view(message):
  """
  Command that outputs random story from database for user response
  """  
  chat_id = message.chat.id
  total_other_stories = 0
  for id in stories:
    total_other_stories += len(stories[id])

  if stories == {}:
    bot.send_message(chat_id, "There are no available stories yet!")
    return

  if chat_id not in viewed_stories:
    viewed_stories[chat_id] = []
    print(len(viewed_stories[chat_id]))

  if len(viewed_stories[chat_id]) == total_other_stories:
    bot.send_message(chat_id, "There are no more stories to view :( Please check back again!")
    return

  # get the id of user to view
  user_id = random.choice(list(stories.keys()))
  # get the story from the chosen user
  story = random.choice(stories[user_id])

  while story in viewed_stories[chat_id]:
    # get the id of user to view
    user_id = random.choice(list(stories.keys()))
    # get the story from the chosen user
    story = random.choice(stories[user_id])

  viewed_stories[chat_id].append(story)
  
  bot.reply_to(message, story)
  sent = bot.send_message(chat_id, "Response to story:")

  def userInput(message):
    open('problem.txt', 'w').write(str(message.chat.id) + ' | ' + message.text + '||')
    bot.send_message(message.chat.id, 'Thank you for your response!')
    bot.send_message(user_id, 'Someone replied to your story: \'' + story + '\':\n\n' + message.text)

  bot.register_next_step_handler(sent, userInput)

@bot.message_handler(commands=['meme'])
def meme(message):
  """
  Command that allows user to find interesting memes
  """
  chat_id = message.chat.id
  img_url = random.choice(memes)

  bot.send_message(message.chat.id, 'Here is a top-tier meme:')

  bot.send_photo(
    chat_id,
    img_url,
  )

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


@bot.message_handler(commands="mood")
def check_in(message):
  chat_id=message.chat.id
  daily_check(chat_id)

def daily_check(chat_id):
  """
  Function that send a daily check-in message to all users
  """
  # for chat_id in user_data:
  bot.send_message(chat_id, "How was your day today?")
  
  buttons = []
  row = []
  for mood in moods:
    button = InlineKeyboardButton(
      text = moods[mood],
      callback_data=mood
    )
    row.append(button)
    
  buttons.append(row)
  
  bot.send_message(
    chat_id=chat_id,
    reply_markup=InlineKeyboardMarkup(buttons),
    text='Choose an emoji according to your mood:'
  )

def daily_check_for_all():
  for chat_id in user_data:
    daily_check(chat_id)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
  """
  Handles the execution of the respective functions upon receipt of the callback query
  """
  chat_id = call.message.chat.id
  data = call.data

  bot.send_photo(chat_id, random.choice(quotes[data]))
  bot.send_message(chat_id, "Would you like to share about your day? Use the /share function!")

schedule.every().day.at("09:00").do(daily_check_for_all)
Thread(target=schedule_checker).start()


@bot.message_handler(regexp="")
def reply(message):
  """
  Command that handles invalid commands
  """
  bot.reply_to(message, 'I don\'t know what you are talking about... Please refer to /help for the list of commands available!')

bot.infinity_polling()
