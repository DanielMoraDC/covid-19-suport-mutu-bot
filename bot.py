#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import messages
from locations import Location
from groups import groups_by_distance

TOKEN = '<telegram_token>'
CLOSEST_GROUPS = 3


def welcome_callback(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=messages.WELCOME)


def find_group_callback(update, context):
    message = update.message
    location = Location(latitude=message.location.latitude,
                        longitude=message.location.longitude)

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

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=response)


def not_location_callback(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=messages.NOT_LOCATION)


# Set token and dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define bot start handler
start_handler = CommandHandler('start', welcome_callback)
dispatcher.add_handler(start_handler)

# On location, retrieve closest group
location_handler = MessageHandler(Filters.location, find_group_callback)
dispatcher.add_handler(location_handler)

# If location not provided, send warning
non_location_handler = MessageHandler(~Filters.location, not_location_callback)
dispatcher.add_handler(non_location_handler)


if __name__ == '__main__':
    updater.start_polling()
