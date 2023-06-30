# Описание класса животное
import user_ex.user_except as uex

__all__ = ["Animal"]


class Animal:
    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        """Основной способ передвижения"""
        raise uex.UserAnimalEmptyMove('Метод передвижения не определен!')

    def say(self):
        """Способ общения, производимые звуки"""
        raise uex.UserAnimalEmptySay()

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.age}"
