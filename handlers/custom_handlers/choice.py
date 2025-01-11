from typing import Any

from loader import bot
from keyboards import replay_keyboards


@bot.message_handler(func=lambda message: message.text == "Готов(а)!")
def choice(message: Any) -> Any:
    """
    Функция предоставляющая выбор категории питомцев пользователю.
    """
    bot.send_message(
        message.chat.id,
        "Выберите категорию:",
        reply_markup=replay_keyboards.choice_kb()
    )
