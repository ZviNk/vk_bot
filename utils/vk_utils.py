from vk_api.longpoll import VkEventType, VkLongPoll

def get_updates(vk, group_id):
    """
    Получение новых событий от VK.
    """
    longpoll = VkLongPoll(vk, group_id)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            return event
