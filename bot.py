import os
from typing import NoReturn
from dotenv import load_dotenv
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from google.cloud import dialogflow


def start_callback(update, context) -> NoReturn:
    update.message.reply_text("Здравствуйте")


def echo(update, context) -> NoReturn:
    message_text = update.message.text
    chat_id = update.message.chat.id
    response_message = detect_intent_texts("technicalsupportassistant-uwyu", chat_id, message_text)
    update.message.reply_text(response_message)


def detect_intent_texts(project_id: str, session_id: str, text) -> str:
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code="ru")
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
    return response.query_result.fulfillment_text


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
