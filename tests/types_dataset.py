USER = {
    "id": 12345678,
    "is_bot": False,
    "first_name": "FirstName",
    "last_name": "LastName",
    "username": "username",
    "language_code": "ru",
}

SUPERGROUP = {
    "id": 12345679,
    "first_name": "FirstName",
    "last_name": "LastName",
    "username": "username",
    "type": "supergroup",
}

PRIVATE_CHAT = {
    "id": 12345678,
    "first_name": "FirstName",
    "last_name": "LastName",
    "username": "username",
    "type": "private",
}

MESSAGE_IN_SUPERGROUP = {
    "message_id": 11223,
    "from": USER,
    "chat": SUPERGROUP,
    "date": 1508709711,
    "text": "Hi, world!",
}

ENTITY_MENTION = {
    "offset": 47,
    "length": 9,
    "type": "mention",
}

ENTITY_BOLD = {
    "offset": 5,
    "length": 2,
    "type": "bold",
}

MESSAGE_WITH_ENTITIES = {
    "message_id": 11223,
    "from": USER,
    "chat": PRIVATE_CHAT,
    "date": 1508709711,
    "text": "Hi, world!",
    "entities": [ENTITY_MENTION]
}

POLL_OPTION_CHICKEN = {
    "text": "chicken",
    "voter_count": 3
}

POLL_OPTION_EGG = {
    "text": "egg",
    "voter_count": 2
}

QUIZ_WITH_ENTITIES = {
    "id": "33334ggd44ttgf4",
    "question": "What was first: chicken or egg?",
    "options": [POLL_OPTION_CHICKEN, POLL_OPTION_EGG],
    "total_voter_count": 5,
    "is_closed": True,
    "is_anonymous": True,
    "type": "quiz",
    "allows_multiple_answers": False,
    "correct_option_id": 1,
    "explanation": ")0)))",
    "explanation_entities": [ENTITY_BOLD]
}

REGULAR_POLL = {
    "id": "33334ggd44ttgf4",
    "question": "What was first: chicken or egg?",
    "options": [POLL_OPTION_CHICKEN, POLL_OPTION_EGG],
    "total_voter_count": 5,
    "is_closed": True,
    "is_anonymous": True,
    "type": "regular",
    "allows_multiple_answers": True,
}

QUIZ = {
    "id": "33334ggd44ttgf4",
    "question": "What was first: chicken or egg?",
    "options": [POLL_OPTION_CHICKEN, POLL_OPTION_EGG],
    "total_voter_count": 5,
    "is_closed": True,
    "is_anonymous": True,
    "type": "quiz",
    "allows_multiple_answers": False,
    "correct_option_id": 1,
    "explanation": ")0)))"
}

MESSAGE_WITH_QUIZ = {
    "message_id": 11223,
    "from": USER,
    "chat": PRIVATE_CHAT,
    "date": 1508709711,
    "poll": QUIZ_WITH_ENTITIES
}

DICE = {
    "value": 6,
    "emoji": "🎲"
}

MESSAGE_WITH_DICE = {
    "message_id": 12345,
    "from": USER,
    "chat": PRIVATE_CHAT,
    "date": 1508768012,
    "dice": DICE
}

USER_123456789 = {
    "id": 123456789,
    "is_bot": False,
    "first_name": "FirstName",
    "last_name": "LastName",
    "username": "username",
    "language_code": "ru",
}

MESSAGE_FROM_123456789 = {
    "message_id": 12345,
    "from": USER_123456789,
    "chat": PRIVATE_CHAT,
    "date": 1508768012,
}

MESSAGE = {
    "message_id": 12345,
    "from": USER,
    "chat": PRIVATE_CHAT,
    "date": 1508768012,
}

CALLBACK_QUERY = {
    "id": "4554tfd44tg",
    "from": USER,
    "message": MESSAGE,
    "chat_instance": "56yhge35tr3",
    "data": "hello world",
}

CALLBACK_QUERY_WITH_DICE_MESSAGE = {
    "id": "4554tfd44tg",
    "from": USER,
    "message": MESSAGE_WITH_DICE,
    "chat_instance": "56yhge35tr3",
    "data": "hello world",
}

CALLBACK_QUERY_IN_SUPERGROUP = {
    "id": "4554tfd44tg",
    "from": USER,
    "message": MESSAGE_IN_SUPERGROUP,
    "chat_instance": "56yhge35tr3",
    "data": "hello world",
}

CALLBACK_QUERY_WITH_MESSAGE_WITH_ENTITIES = {
    "id": "4554tfd44tg",
    "from": USER,
    "message": MESSAGE_WITH_ENTITIES,
    "chat_instance": "56yhge35tr3",
    "data": "hello world",
}

CALLBACK_QUERY_WITH_QUIZ_MESSAGE = {
    "id": "4554tfd44tg",
    "from": USER,
    "message": MESSAGE_WITH_QUIZ,
    "chat_instance": "56yhge35tr3",
    "data": "hello world",
}

CALLBACK_QUERY_FROM_123456789 = {
    "id": "4554tfd44tg",
    "from": USER_123456789,
    "message": MESSAGE,
    "chat_instance": "56yhge35tr3",
    "data": "hello world",
}
