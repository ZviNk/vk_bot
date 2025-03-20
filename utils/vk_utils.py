from vk_api.longpoll import VkEventType, VkLongPoll

def get_updates(vk, group_id):
    """
    Получение новых событий от VK.
    """
    longpoll = VkLongPoll(vk, group_id)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            return event


def send_message(vk, peer_id, message):
    """
    Отправка сообщения в чат.

    :param vk: объект API VK (например, экземпляр vk_api.VkApi)
    :param peer_id: идентификатор чата или пользователя
    :param message: текст сообщения для отправки
    """
    vk.messages.send(
        peer_id=peer_id,
        message=message,
        random_id=random.randint(0, 2 ** 31)
    )