import telebot
from func import do_ad
import time

bot = telebot.TeleBot('YourTelegramToken')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Send me text of your ad and I'll do with it something")

@bot.message_handler(content_types=['text', 'sticker'])
def send_text(message):
    ch = do_ad(message.text)
    while not ch:
        time.sleep(1)
    bot.send_message(message.chat.id, "Your ad:")
    bot.send_photo(message.chat.id, open(ch, 'rb'))
    bot.send_sticker(message.chat.id, 'CAADAgADTAMAAkcVaAkmOU8hWPR0YhYE')

bot.polling()
