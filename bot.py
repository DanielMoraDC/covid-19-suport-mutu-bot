import telebot

import messages
from locations import Location
from groups import groups_by_distance

TOKEN = '<telegram_token>'
bot = telebot.TeleBot(TOKEN)

CLOSEST_GROUPS = 3


@bot.message_handler(commands=['info'])
def welcome_message(message):
    bot.register_next_step_handler(message, buscar_grup)
    bot.reply_to(message, messages.WELCOME.encode('utf-8'))


@bot.message_handler()
def buscar_grup(message):
    if message.content_type == 'location':
        location = Location(latitude=message.json['location']['latitude'],
                            longitude=message.json['location']['longitude'])

        groups = groups_by_distance(location)
        closest = groups[:CLOSEST_GROUPS]
        groups_display_str = '\n'.join(list(map(str, closest)))

        if closest[0].distance > 1.0:
            response = messages.LOCATIONS_CLOSE_TEMPLATE_NOK.format(
                group_info=groups_display_str
            )
        else:
            response = messages.LOCATIONS_CLOSE_TEMPLATE_OK.format(
                group_info=groups_display_str
            )

    else:
        response = messages.NOT_LOCATION

    bot.reply_to(message, response.encode('utf-8'))
    bot.register_next_step_handler(message, buscar_grup)

bot.polling()
