import telebot

bot = telebot.TeleBot("7192985837:AAEq92u7m49Rk4HEm89PXzw0mnqvPAlvYcg")

@bot.message_handler(commands=["start"])
def hello (message):
   bot.send_message(message.chat.id, "Привет я бот tapok мои команды: /dontclick /coll /joke /name")

@bot.message_handler(commands=["dontclick"])
def tapok(message):
   bot.send_message(message.chat.id, "[Не нажимай](https://www.youtube.com/watch?v=GBIIQ0kP15E)", parse_mode="Markdown")

@bot.message_handler(commands=["coll"])
def coll(message):
   bot.send_message(message.chat.id, "**Ты крутой)**", parse_mode="Markdown")
   bot.send_message(message.chat.id, "Пожалуйста)))")

@bot.message_handler(commands=["joke"])
def joke(message):
   bot.send_message(message.chat.id, "ооо хочешь анекдот?")
   bot.send_message(message.chat.id, "ну ладно)")
   bot.send_message(message.chat.id, "Колобок повесился")
   bot.send_message(message.chat.id, "Хахахахах")
   bot.send_message(message.chat.id, "смешно?")

@bot.message_handler(commands=["name"])
def name(message):
   bot.send_message(message.chat.id, "Имя моего создателя: Дмитрий он очень классный парень")

bot.infinity_polling()