import telebot
import config 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text == "Kто ты?":
        bot.send_message(message.from_user.id, "Я тестовый чатбот для учебного примера.")
    elif message.text == "Как тебя зовут?":
        bot.send_message(message.from_user.id, "Меня зовут MyFirstTestBot.")
    elif message.text == "Что ты умеешь?":
        bot.send_message(message.from_user.id, "Я умею отвечать на несколько простых вопросов - кто я, как меня зовут и что я умею делать.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши что-то другое.")

bot.polling(none_stop=True, interval=0)
