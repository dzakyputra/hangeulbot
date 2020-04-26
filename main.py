from telegram.ext import Updater, CommandHandler
import pandas as pd
import logging


# Set the logging function to print the error message whenever it happens
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.ERROR)


def send_word(update, context):
  
  # Read the dataset and pick a random word
  dictionary = pd.read_csv('dictionary.csv')
  word = dictionary['word'].sample(1).values[0]
  
  # Get the user chat_id for sending back the message
  chat_id = update.message.chat_id
  
  # Send the word and the audio
  context.bot.send_message(chat_id=chat_id, text=word)
  context.bot.send_voice(chat_id=chat_id, voice=open('audio/{}.mp3'.format(word), 'rb'))
  
def main():
  
  # Initiate the bot and add command handler  
  updater = Updater('YOUR_BOT_TOKEN', use_context=True)
  updater.dispatcher.add_handler(CommandHandler('word', send_word))
  
  # Run the bot
  updater.start_polling()
  updater.idle()
  
if __name__ == '__main__':
  main()