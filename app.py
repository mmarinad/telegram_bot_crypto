
import telebot
from config import keys, TOKEN
from utils import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу, введите команду боту в следующем формате:\n<имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text += f"\n{key}"
    bot.reply_to(message, text)



@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(" ")

    if len(values) != 3:
        raise ConvertionException('Неверное количество параметров!')
        
    quote, base, amount = values
    
    total_base = CryptoConverter.convert(quote, base, amount)
    text = f'Цена {amount}  {base} в {quote} - {total_base}'

    bot.send_message(message.chat.id, text)

bot.polling()