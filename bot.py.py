import telebot
import config 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == "Старт":
        bot.send_message(message.from_user.id, 'Привет !')
    elif message.text == "что ты уммешь делать? ":
        bot.send_message(message.from_user.id, " Я телеграм бот и я умею отвечать на несколько простых вопросов ")
    elif message.text == "далее":
        bot.send_message(message.from_user.id, "")
    elif message.text == "Как тебя зовут?":
        bot.send_message(message.from_user.id, "Меня зовут MyFirstTestBot.")
    elif message.text == "Что ты умеешь?":
        bot.send_message(message.from_user.id, "Я умею отвечать на несколько простых вопросов - кто я, как меня зовут и что я умею делать.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши что-то другое.")

bot.polling(none_stop=True, interval=0)
