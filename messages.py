from hero import Hero


class Messages:
    @staticmethod
    def start_message():
        return "Добро пожаловать, друг! Мы подберем для тебя идельного героя " \
               "Dota 2. И так, поехали!\n\nСколько у тебя часов в игре?"

    @staticmethod
    def new_start_message():
        return "Можем подобрать героя еще раз\n\nСколько у тебя часов в игре?"

    @staticmethod
    def please_repeat():
        return "Нет такого варианта ответа, выбери из предложенных ниже"

    @staticmethod
    def select_position():
        return "На какой позиции ты хочешь играть?"

    @staticmethod
    def select_category():
        return "Какую категорию предпочитаешь?"

    @staticmethod
    def answer(hero: Hero):
        return f"Вот что мы подобрали:\n" \
               f"{hero.description}"

    @staticmethod
    def answer_not_found():
        return "Такого пока нет"
