# Covid Suport Mutu Catalunya

This purpose of this bot is to retrieve the closest mutual aid group given 
the user's location in Catalonia.

# Development

You need to install the requirements, making sure the following are installed:

- Python >= 3.7
- Virtualenv >= 15.1.0

Then, create a virtual environment (e.g. named venv):

```shell script
virtualenv --python=python3.7 venv
```

Activate and install dependencies:

```shell script
source venv/bin/activate
```

Then you can run bot by typing:

```shell script
TELEGRAM_BOT_TOKEN=<telegram-token> bot.py
```

Make sure you use a proper Telegram Bot Token `<telegram-token>`.
Follow instructions in [here](https://core.telegram.org/bots) to create one.

# Deployment

In order to be able to configure CD on this bot, you need to [configure two Github secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets):

- HEROKU_API_KEY. Instructions on how to generate key for your app, [here](https://help.heroku.com/PBGP6IDE/how-should-i-generate-an-api-key-that-allows-me-to-use-the-heroku-platform-api).
- HEROKU_APP_NAME. Name of the Heroku app you want to use for the bot.

# Future work

1. Automatic detection of groups and locations (i.e. we are hard-coding them now).
