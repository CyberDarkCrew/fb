from sqlalchemy import true
from info import *
from reply import *

bot = telebot.TeleBot(token_bot)
@bot.message_handler(func=lambda m : True)
def rm(m):
    replys(m)
    
bot.infinity_polling()
