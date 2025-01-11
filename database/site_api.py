from bs4 import BeautifulSoup
import requests


url = "https://newdomcat.ru/%d0%ba%d0%be%d1%88%d0%ba%d0%b8-%d0%b8-%d0%ba%d0%be%d1%82%d1%8b/"

req = requests.get(url)
src = req.text
soup = BeautifulSoup(src, "lxml")




def category_cats(cats_age: str) -> list[str]:
    """Категории кошек(Взрослые коты, взрослые кошки, котята)"""
    cats = []
    choice_age_cats = soup.find_all(class_="elementor-widget-image")
    if cats_age == "Кошки":
        cats = ["Кошки", choice_age_cats[0].find("a").get("href")]
    elif cats_age == "Коты":
        cats = ["Коты", choice_age_cats[1].find("a").get("href")]
    elif cats_age == "Котята":
        cats = ["Котята", choice_age_cats[2].find("a").get("href")]
    return cats


def catalog_cats(cat: list[str]) -> list[list]:
    """
    Функция для отбора и распределения нужной информации с сайта
    :param cat: list(str) с названием категории кошек и ссылкой на нее
    :return: list[list] список с информацией о каждой кошке
    """
    req_for_catalog = requests.get(cat[1])
    src_for_catalog = req_for_catalog.text
    soup_for_catalog = BeautifulSoup(src_for_catalog, "lxml")

    cats_info = []
    all_catalog = soup_for_catalog.find_all(class_="elementor-widget-wrap")
    for i_count in range(len(all_catalog) - 7):
        photo = all_catalog[i_count].find(class_="elementor-widget-image").find("img").get("src")
        name = all_catalog[i_count].find("h2").text
        in_shelter = all_catalog[i_count].find(class_="elementor-headline-dynamic-text").text
        bio = all_catalog[i_count].find("h6").text.split("Возраст")
        url_page = all_catalog[i_count].find(class_="elementor-button-wrapper").find("a").get("href")
        cats_info.append([photo, name, in_shelter, bio, url_page])
    return cats_info
#       age = bio[1] - возраст кошки
