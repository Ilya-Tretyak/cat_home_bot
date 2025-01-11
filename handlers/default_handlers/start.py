from telebot.types import Message

from loader import bot

from peewee import IntegrityError
from database.model import User
from keyboards import replay_keyboards


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    """Приветственное сообщение. Бот собирает информацию о пользователе, записывая ее в базу данных."""
    bot.delete_message(message.chat.id, message.message_id)
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        bot.send_message(
            message.chat.id,
            f"\nДобро пожаловать в 'Новый Дом'!👋"
            f"\nС помощью этого бота ты сможешь выбрать и помочь нашим дорогим кошачьим друзьям. "
            f"\nГотов(а) начать?",
            reply_markup=replay_keyboards.hello_kb()
        )
    except IntegrityError:
        bot.send_message(
            message.chat.id,
            f"Рад вас снова видеть {message.from_user.first_name}!"
            f"\nГотов(а) начать?",
            reply_markup=replay_keyboards.hello_kb()
        )
