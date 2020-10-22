!pip install adafruit-io
import os
x = os.getenv('nikhila_3010')
y = os.getenv('aio_EIjL79FGgDc4hGvhB34GgCqJZVPW')
from Adafruit_IO import Client, Feed
aio = Client(x,y)
new = Feed(name='bot')
result = aio.create_feed(new)
 from  import DataAdafruit_IO
!pip install python-telegram-bot
from Adafruit_IO import Client,Data
from telegram.ext import Updater,CommandHandler
def on(bot,update):
  chat_id = update.message.chat_id    
  aio.create_data('bot',Data(value = 1))
  bot.send_message(chat_id =chat_id,text ="Lights On")
  def off(bot,update):
  chat_id = update.message.chat_id
  aio.create_data('bot',Data(value = 0))
  bot.send_message(chat_id =chat_id,text ="Lights Off")
  updater =Updater('1323642446:AAE1MdzDxZjeynYpTL7I4zFg6W_Pp4cQ0MA')
dp = updater.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
updater.start_polling()
updater.idle()
