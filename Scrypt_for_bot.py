import telebot

token_API = "7076388063:AAFbcBndtPnfr0wh33UWtRTk5IuQY2LrMG4"
bot = telebot.TeleBot(token_API)

@bot.message_handler(commands = ['start'])
def start(message):
    #print(message.user_id)
    bot.send_message(message.chat.id, 'привет!')



bot.polling(none_stop = True)