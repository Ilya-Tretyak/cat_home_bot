<img src="database/pictures/logo.png" alt="bot logo" width="200px">

__NewHomeBot__: 
Телеграм бот приюта ["Новый Дом"](https://newdomcat.ru/)


Что это за бот?
---
____
__<p style="color: chartreuse">NewHomeBot</p>__  -это телеграм бот, созданный для поддержки кошачьего приюта в поиске дома для животных, а так же для легкого и
доступного выбора питомца потенциальным хозяевам.

Быстрый старт
---
____
+ Сохранить папку с проектом на своем устройстве или воспользуйтесь виртуальным хостингом
+ В файле <font color="chartreuse">.env_template</font> введите токен бота и измените название на <font color="chartreuse">.env</font>
+ Создать виртуальное окружение и запустить его:
  ```
  python -m venv venv
  ```
  ```
  venv/Scripts/activate
  ```
+ Запустите python-файл <font color="chartreuse">main.py</font>
+ В [Telegram](https://web.telegram.org/) найдите бота [@NewDomCatBot](https://web.telegram.org/a/#6505985357)\

<font size = "4" color = "green">Готово! Теперь можно пользоваться ботом.</font>

Зависимости
---
____
При создании бота использовались:
1. <font size = "4">Для парсинга сайта:</font>
   + __Библиотека Requests__ для работы с запросами на нужный адрес сайта;
    ```python
    import requests

    url = "https://newdomcat.ru/%d0%ba%d0%be%d1%88%d0%ba%d0%b8-%d0%b8-%d0%ba%d0%be%d1%82%d1%8b/"
    req = requests.get(url)
    src = req.text
    ```
   + __Библиотека Beautiful Soup__ для работы с HTML-кодом;
    ```python
    from bs4 import BeautifulSoup
    import requests


    url = "https://newdomcat.ru/%d0%ba%d0%be%d1%88%d0%ba%d0%b8-%d0%b8-%d0%ba%d0%be%d1%82%d1%8b/"

    req = requests.get(url)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    ```
2. <font size = "4">Для базы данных:</font>
    + __Peewee__ ORM позволяющая работать с базами данных, не делая ручных запросов;
   ```python
   from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    IntegerField,
    TextField)
   
    class BaseModel(Model):
        class Meta:
            database = db

    ```
3. Для реализации бота:
    + __Библиотека pyTelegramBotAPI (telebot)__ для создания и настройки логики бота;
   ```python
   from telebot import TeleBot
   from telebot.storage import StateMemoryStorage
   from config_data import config

   storage = StateMemoryStorage()
   bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
   ```
