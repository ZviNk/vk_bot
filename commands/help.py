def handle(event, vk_session):
    vk_session.method('messages.send', {
        'user_id': event.user_id,
        'message': 'Доступные команды:\n/start - старт\n/help - помощь',
        'random_id': 0
    })
