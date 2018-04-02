import telebot

import settings

bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)


@bot.message_handler(func=lambda message: message.forward_from is not None)
def get_forwarded_message(message):
    print message


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Hi! Share your contacts please!')


@bot.message_handler(content_types=["contact"])
def get_contact(message):
    print message.contact.phone_number
    if '+' + message.contact.phone_number == '+79990001122':
        bot.send_message(message.chat.id, 'You had already registered, faggot')
    else:
        bot.send_message(message.chat.id, 'Successfully sent! You can use system :)')


if __name__ == '__main__':
    bot.polling(none_stop=True)
