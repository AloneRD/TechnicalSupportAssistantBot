import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="vk1.a.BxE87b-9oWfUBcdw2eLN4TFz_6UQ7BoIocp-KqptmCmYigE4TWOb4GMSI9ub-Psytdw6G_xXL0QB8LAEh2I1hDmEcjc9it9cwnyWw7Rz-G_V5NS1-19hRUubDiRZPeeROHa8tHvOX2uYsZAiS2gtvODaS6Py5LeOs5MwnONK2mBDgOSjdUuqV30QiPCjfhLq")

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Новое сообщение:')
        if event.to_me:
            print('Для меня от: ', event.user_id)
        else:
            print('От меня для: ', event.user_id)
        print('Текст:', event.text)