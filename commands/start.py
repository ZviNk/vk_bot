def handle(event, vk_session):
    vk_session.method('messages.send', {
        'user_id': event.user_id,
        'message': 'Привет! Я бот. Напиши /help для помощи.',
        'random_id': 0
    })
