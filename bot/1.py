from telebot import TeleBot

token = "7678825823:AAEthC5IuPM7tllfuikllMSt8qH9GPcirHQ"
bot = TeleBot(token)
@bot.message_handler(commands="start")
def start(message):
    chat_id = message.chat.id
    username =  message.from_user.username
    print(username)
    print(chat_id)
    bot.send_message(chat_id, "Salom Qalisan")
    bot.send_message(chat_id, "Salom")
    bot.send_message(chat_id,  "Mening sening chat ID bor")
bot.polling(none_stop=True)