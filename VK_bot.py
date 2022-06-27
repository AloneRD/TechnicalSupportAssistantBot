import vk_api as vk
import os
import random
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
from google.cloud import dialogflow
from google_dialog_flow_api import detect_intent_texts


def callback_bot(event, vk_api):
    response_message = detect_intent_texts("technicalsupportassistant-uwyu", event.user_id, event.text, "vk")
    try:
        vk_api.messages.send(
            user_id=event.user_id,
            message=response_message,
            random_id=random.randint(1, 1000)
        )
    except:
        pass


if __name__ == "__main__":
    load_dotenv()
    vk_token = os.getenv("VK_TOKEN")
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            callback_bot(event, vk_api)
