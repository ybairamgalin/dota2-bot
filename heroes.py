import random

from user import User
from hero import Hero

import heroes_list


class HeroNotFound(Exception):
    pass


class Heroes:
    heroes = []

    def __init__(self):
        self.heroes = heroes_list.heroes

    def get(self, user: User):
        """Функция принимает объект типа User и возвращает подходящего
        пользователю user героя"""
        possible_answers = []
        print(user)

        for hero in self.heroes:
            if hero.time_needed == user.hours and hero.role == user.role and \
                    hero.category == user.category:
                possible_answers.append(hero)

        if len(possible_answers) == 0:
            raise HeroNotFound

        return possible_answers[random.randint(0, len(possible_answers) - 1)]
