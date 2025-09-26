import telebot

token_API = "sosi"
bot = telebot.TeleBot(token_API)

@bot.message_handler(commands = ['start'])
def start(message):
    #print(message.user_id)
    bot.send_message(message.chat.id, 'привет!')




bot.polling(none_stop = True)
