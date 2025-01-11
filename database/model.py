import os

from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    IntegerField,
    TextField)

from database.site_api import catalog_cats, category_cats


db = SqliteDatabase(r"../cat_home_bot/database/cats_info.db")


class BaseModel(Model):
    """Базовый класс для всех моделей"""
    class Meta:
        database = db


class User(BaseModel):
    """
    Класс с информацией о пользователях.
    Идентификатор, никнейм, имя, фамилия.
    """
    class Meta:
        db_table = "Users"

    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)


class CatMale(BaseModel):
    """
    Класс с информацией о взрослых котах.
    Фотография, имя, возраст, время проведенное в приюте, биография, ссылка на сайте.
    """
    class Meta:
        db_table = "Cat_Male"

    photo = TextField()
    name = CharField()
    age = IntegerField()
    in_shelter = IntegerField()
    bio = TextField()
    url = TextField()


class CatFemale(BaseModel):
    """
    Класс с информацией о взрослых кошках.
    Фотография, имя, возраст, время проведенное в приюте, биография, ссылка на сайте.
    """
    class Meta:
        db_table = "Cat_Female"

    photo = TextField()
    name = CharField()
    age = IntegerField()
    in_shelter = IntegerField()
    bio = TextField()
    url = TextField()


class Kitten(BaseModel):
    """
    Класс с информацией о котятах.
    Фотография, имя, возраст, время проведенное в приюте, биография, ссылка на сайте.
    """
    class Meta:
        db_table = "Kitten"

    photo = TextField()
    name = CharField()
    age = IntegerField()
    in_shelter = IntegerField()
    bio = TextField()
    url = TextField()


db.create_tables([CatMale, CatFemale, Kitten, User])


def update_database(current_model, cats):
    """
    Функция для обновления информации базы данных.
    :param current_model: Класс питомцев (class)
    :param cats: Список питомцев (list)
    :return:Any
    """
    cats_list = catalog_cats(cats)
    for i_cat in cats_list:
        cat = current_model(
            photo=i_cat[0],
            name=i_cat[1],
            age=i_cat[3][1],
            in_shelter=i_cat[2],
            bio=i_cat[3][0],
            url=i_cat[4]
        )
        cat.save()


update_database(CatMale, category_cats("Коты"))
update_database(CatFemale, category_cats("Кошки"))
update_database(Kitten, category_cats("Котята"))
