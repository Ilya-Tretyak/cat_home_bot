from loader import bot
from keyboards import inline_keyboards
from database.model import CatMale, CatFemale, Kitten
from .choice import choice

import time
import os

count = 1
catalog_list = Kitten


@bot.message_handler(func=lambda message: message.text in ["Кошки", "Котята", "Коты"])
def cat_catalog(message) -> None:
    """
    Хендлер выбора категории в боте
    :param message: str(Кошки, Коты, Котята)
    :return: class
    """
    global count, catalog_list

    if message.text == "Кошки":
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        count = 1
        catalog_list = CatFemale
    elif message.text == "Котята":
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        count = 1
        catalog_list = Kitten
    elif message.text == "Коты":
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        count = 1
        catalog_list = CatMale

    """Бот отсылает сообщение пользователю с информацией о выбранной категории """
    bot.send_photo(
        message.chat.id,
        photo=catalog_list.get(id=count).photo,
        caption=f"Имя: {catalog_list.get(id=count).name}"
                f"\nВозраст: {catalog_list.get(id=count).age}"
                f"\nВ приюте: {catalog_list.get(id=count).in_shelter}"
                f"\nО питомце: {catalog_list.get(id=count).bio}",
        reply_markup=inline_keyboards.navigation_kb()
    )

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        """Функция реализующая работу InLine - клавиатуры"""
        global count
        if call.data == "next-page":
            if count < catalog_list.select().count():
                bot.delete_message(call.message.chat.id, call.message.message_id)
                count += 1
                bot.send_photo(
                    call.message.chat.id,
                    photo=catalog_list.get(id=count).photo,
                    caption=f"Имя: {catalog_list.get(id=count).name}"
                            f"\nВозраст: {catalog_list.get(id=count).age}"
                            f"\nВ приюте: {catalog_list.get(id=count).in_shelter}"
                            f"\nО питомце: {catalog_list.get(id=count).bio}",
                    reply_markup=inline_keyboards.navigation_kb()
                )
        elif call.data == "back-page":
            if count > 1:
                bot.delete_message(call.message.chat.id, call.message.message_id)
                count -= 1
                bot.send_photo(
                    message.chat.id,
                    photo=catalog_list.get(id=count).photo,
                    caption=f"Имя: {catalog_list.get(id=count).name}"
                            f"\nВозраст: {catalog_list.get(id=count).age}"
                            f"\nВ приюте: {catalog_list.get(id=count).in_shelter}"
                            f"\nО питомце: {catalog_list.get(id=count).bio}",
                    reply_markup=inline_keyboards.navigation_kb()
                )
        elif call.data == "want-to-take":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_photo(
                message.chat.id,
                photo=open(os.path.abspath("database/pictures/img_for_rule.png"), "rb"),
                caption="Прежде чем вы отправите анкету потенциального хозяина,"
                        " ознакомьтесь с обязательными правилами!",
                reply_markup=inline_keyboards.rule_kb()
            )

        if call.data == "back":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            choice(message)

        if call.data == "rule_true":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_photo(
                call.message.chat.id,
                photo=open(os.path.abspath("database/pictures/img_for_blank.jpg"), "rb"),
                caption="Спасибо, что изучили правила!"
                        "Осталось только заполнить анкету.",
                reply_markup=inline_keyboards.blank_kb()
            )
            time.sleep(5)
            bot.send_message(message.chat.id, "Если вы хотите посмотреть больше питомцев, воспользуйтесь кнопкой меню "
                                              "в левом, нижнем углу!")
