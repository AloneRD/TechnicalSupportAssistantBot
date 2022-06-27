import os
from typing import NoReturn
from dotenv import load_dotenv
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
import telegram
import logging
from google_dialog_flow_api import detect_intent_texts

logger = logging.getLogger("TGBot")


class TelegramLogsHandler(logging.Handler):

    def __init__(self, token, chat_id) -> None:
        super().__init__()
        self.bot = telegram.Bot(token)
        self.chat_id = chat_id

    def emit(self, record) -> None:
        log_entry = self.format(record)
        self.bot.send_message(chat_id=self.chat_id, text=log_entry)


def start_callback(update, context) -> NoReturn:
    update.message.reply_text("Здравствуйте")


def responds_to_user(update, context) -> NoReturn:
    try:
        message_text = update.message.text
        chat_id = update.message.chat.id
        response_message = detect_intent_texts(project_id, chat_id, message_text, 'tg')
        update.message.reply_text(response_message)
    except:
        logger.exception("Бот упал с ошибкой")


def main():
    load_dotenv()
    global project_id
    tg_token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.environ.get("TG_CHAT_ID")
    project_id = os.getenv("PROJECT_ID_DIALOG_FLOW")

    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramLogsHandler(tg_token, chat_id))

    updater = Updater(token=tg_token)
    dispacher = updater.dispatcher

    dispacher.add_handler(CommandHandler("start", start_callback))
    dispacher.add_handler(MessageHandler(Filters.text, responds_to_user))

    updater.start_polling()


if __name__ == '__main__':
    main()
