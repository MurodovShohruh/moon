from telebot import TeleBot
from telebot import types

token = "7678825823:AAEthC5IuPM7tllfuikllMSt8qH9GPcirHQ"

bot = TeleBot(token)

@bot.message_handler(commands="start")
def start(message):
    chat_id = message.chat.id
    # keyboard=types.ReplyKeyboardMarkup()
    # salom=types.KeyboardButton(text="Salom")
    # asc=types.KeyboardButton(text="Xayr")
    # keyboard.add(salom,asc)
    
    markub=types.InlineKeyboardMarkup()
    moon= types.InlineKeyboardButton("Moon", callback_data="Moon")
    markub.add(moon)
    bot.send_message(chat_id,"Assalom alaykum",reply_markup=markub)

    bot.register_next_step_handler(message, show_inline)
    
def show_inline(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"MOON")
    
bot.polling(none_stop=True)