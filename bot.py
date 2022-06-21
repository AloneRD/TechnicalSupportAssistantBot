import os
from dotenv import load_dotenv
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters


def start_callback(update, context):
    update.message.reply_text("Здравствуйте")


def echo(update, context):
    message_text = update.message.text
    update.message.reply_text(message_text)


def main():
    load_dotenv()
    tg_token = os.getenv("TELEGRAM_TOKEN")

    updater = Updater(token=tg_token)
    dispacher = updater.dispatcher

    dispacher.add_handler(CommandHandler("start", start_callback))
    dispacher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()


if __name__ == '__main__':
    main()
