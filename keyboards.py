from telegram import ReplyKeyboardMarkup


class Keyboards:
    @staticmethod
    def start_keyboard():
        keyboard = [
            ["<100", "100-500"],
            ["500-1000", ">1000"]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def position():
        keyboard = [
            ["1", "2"],
            ["3", "4", "5"]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    @staticmethod
    def category():
        keyboard = [
            ["Сила"], ["Ловкость"], ["Интеллект"]
        ]
        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
