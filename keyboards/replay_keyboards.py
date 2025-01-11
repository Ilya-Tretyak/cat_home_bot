from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def hello_kb():
    """
    Клавиатура приветственного сообщения
    """
    markup_hello = ReplyKeyboardMarkup(True, True)
    button = KeyboardButton("Готов(а)!")
    return markup_hello.add(button)


def choice_kb():
    """
    Клавиатура с выбором категории животных
    """
    markup_choice = ReplyKeyboardMarkup(True, True)
    button_cat_male = KeyboardButton("Коты")
    button_cat_female = KeyboardButton("Кошки")
    button_kitten = KeyboardButton("Котята")
    return markup_choice.add(button_cat_male, button_cat_female, button_kitten)
