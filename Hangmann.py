import re
from random import choice as random_choice
from lib.take_word import downloads_russian_words

def проверить_алфавит(char: str) -> bool:
    """
    Проверяет, состоит ли строка только из букв алфавита (латинского и кириллического)
    и пробелов.

    Параметры:
    char -- символ, который нужно проверить

    Возвращает:
    True, если строка состоит только из букв алфавита и пробелов, False в противном случае.
    """

def информация_игры() -> None:
    """
    Выводит информацию о текущем состоянии игры.

    Возвращает:
    None
    """

def печать_информации_игры(
    word_list: tuple,
    guess_word_list: list,
    unguessed_set: set,
    guess_chance: int
) -> str:  
    """
    Выводит информацию о текущем состоянии игры.

    Параметры:
    word_list: tuple -- загаданное слово
    guess_word_list: list -- список букв, которые были угаданы
    unguessed_set: set -- неправильные буквы
    guess_chance: int -- оставшиеся попытки

    Возвращает:
    str -- информация о текущем состоянии игры
    """

def игровая_логика(
    word_list: tuple,
    guess_word_list: list,
    guessed_letters: set,
    unguessed_letters: set,
    input_letter: str,
    guess_chance: int,
) -> int: 
    """
    Обновляет список угаданных слов и множество непредсказанных букв на основе введенной буквы.
    Затем выводит информацию об игре.
    Параметры:
        word_list (tuple): Кортеж, содержащий слова, которые нужно угадать.
        guess_word_list (list): Список, представляющий текущее состояние угаданного слова.
        guessed_letters (set): Множество, содержащее угаданные буквы.
        unguessed_letters (set): Множество, содержащее неугаданные буквы.
        input_letter (str): Буква, введенная игроком.
        guess_chance (int): Количество попыток, которые у игрока есть для угадывания слова.
    Возвращает:
        int -- Количество оставшихся попыток.
    """

def обновление_списка_угаданных_слов(
    word_list: tuple, 
    guess_word_list: list, 
    guessed_letters: set, 
    input_letter: str
) -> None:
    """
    Обновляет список угаданных слов на основе входной буквы.

    Параметры:
    - word_list (список): Список слов.
    - guess_word_list (список): Список, представляющий текущее состояние угаданного слова.
    - guessed_letters (множество): Множество букв, которые уже были угаданы.
    - input_letter (строка): Буква, которую нужно проверить и добавить в список угаданного слова.

    Возвращает:
    - None

    Примечание:
    - Эта функция перебирает список слов и обновляет список угаданных слов и множество угаданных
    букв на основе входной буквы.
    """

def обновление_неправильных_букв(
    word_list: tuple, 
    input_letter: str, 
    unguessed_letters: set, 
    guess_chance: int
) -> int:
    """
    Обновляет множество незагаданных букв и уменьшает количество попыток угадывания.

    Параметры:
        word_list (list): Список слов, с которыми происходит сравнение.
        input_letter (str): Буква, введенная пользователем.
        unguessed_letters (set): Множество букв, которые еще не были угаданы.
        guess_chance (int): Количество оставшихся попыток.

    Возвращает:
        int -- Количество оставшихся попыток.
    """

if __name__ == "__main__":
    game_info()
    WORD_LIST: tuple = tuple(
        random_choice(downloads_russian_words()).lower()
    )
    attempt: int = len(WORD_LIST)  # type: ignore

    GUESS_WORD_LIST: list = ["_" for _ in WORD_LIST]

    guessed_set: set = set()  # type: ignore
    unguessed_set: set = set()  # type: ignore

    while (guessed_set != set(GUESS_WORD_LIST)) and (attempt > 0):
        input_letter = input("Введите букву русского алфавита: ")

        if check_alphabet(input_letter) and len(input_letter) == 1:
            attempt = game_logic(
                WORD_LIST,
                GUESS_WORD_LIST,
                guessed_set,
                unguessed_set,
                input_letter,
                attempt,
            )
        else:
            print("Попробуйте ещё раз, вводите только буквы русского языка.")
