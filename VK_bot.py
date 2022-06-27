import vk_api as vk
import os
import random
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
from google_dialog_flow_api import detect_intent_texts


def responds_to_user(event, vk_api):
    response_message = detect_intent_texts(project_id, event.user_id, event.text, "vk")
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
    global project_id
    vk_token = os.getenv("VK_TOKEN")
    project_id = os.getenv("PROJECT_ID_DIALOG_FLOW")
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            responds_to_user(event, vk_api)
