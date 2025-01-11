from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def navigation_kb():
    """
    Клавиатура для навигации по списку животных.
    ('Вперед', 'Назад', 'Вернутся')
    """
    markup_for_navigation = InlineKeyboardMarkup()
    markup_for_navigation.add(InlineKeyboardButton(text="Вернутся ↩", callback_data="back"))
    markup_for_navigation.add(
        InlineKeyboardButton(text="⬅Назад", callback_data="back-page"),
        InlineKeyboardButton(text="Вперед➡", callback_data="next-page")
    )
    return markup_for_navigation.add(InlineKeyboardButton(text="---Хочу забрать---", callback_data="want-to-take"))


def rule_kb():
    """
    Клавиатура с обязательными правилами
    """
    markup_for_rule = InlineKeyboardMarkup(row_width=1)
    url_rule = "https://newdomcat.ru/%d0%b7%d0%b0%d0%b1%d1%80%d0%b0%d1%82%d1%8c-%d0%ba%d0%be%d1%88%d0%ba%d1%83/"
    return markup_for_rule.add(
        InlineKeyboardButton(text="⚠Обязательные правила⚠", url=url_rule),
        InlineKeyboardButton(text="С правилами ознакомлен✅", callback_data="rule_true")
    )


def blank_kb():
    """
    Клавиатура для анкеты потенциального хозяина
    """
    markup_for_blank = InlineKeyboardMarkup()
    url_blank = \
        "https://docs.google.com/forms/d/e/1FAIpQLSen7c2UIzhXLh46G6hkDbsJhleDVrgGNGLiDKgC1Cyb_LcYmg/viewform"
    return markup_for_blank.add(InlineKeyboardButton(text="📃Анкета📃", url=url_blank))
