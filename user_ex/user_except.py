class UserMainException(Exception):
    """Базовое пользовательское исключение."""
    pass


class UserAnimalEmptySay(UserMainException):
    """Исключение неопределенного метода say."""

    def __init__(self, value=None):
        self.value = value if value is not None else \
            "Не определен метод разговаривания животного say."

    def __str__(self):
        return self.value


class UserAnimalEmptyMove(UserMainException):
    """Исключение неопределенного метода move"""

    def __init__(self, value=None):
        self.value = value if value is not None else \
            "Не определен метод перемещения животного в пространстве move."

    def __str__(self):
        return self.value


class UserChessPositionWrong(UserMainException):
    """Исключение неверной комбинации ферзей."""

    def __init__(self, value=None):
        self.value = value if value is not None else 'Комбинация неверна!'

    def __str__(self):
        return self.value
