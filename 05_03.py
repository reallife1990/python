# Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх
# списков (по одному из каждого):

# Документировать код функции.

# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
import random


def get_jokes(number,origin):
    for _ in range(number):
        if origin == 1:
            if len(adverbs) == 0 or len(nouns) == 0 or len(adjectives) == 0:
                print("Пардон, шутки закончились(((")
                break
        # print(nouns[random.randint(0, len(nouns)-1)])
        # print(adverbs[random.randint(0, len(adverbs) - 1)])
        # print(adjectives[random.randint(0, len(adjectives) - 1)])
            print(f"{nouns.pop(random.randint(0, len(nouns)-1))} "
                f"{adverbs.pop(random.randint(0, len(adverbs) - 1))} "
                f"{adjectives.pop(random.randint(0, len(adjectives) - 1))}")
        else:
            print(f"{nouns[random.randint(0, len(nouns) - 1)]} "
                  f"{adverbs[random.randint(0, len(adverbs) - 1)]} "
                  f"{adjectives[random.randint(0, len(adjectives) - 1)]}")


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(int(input("Введите количество шуток: ")),
          int(input("быть оригинальным? (да-1/нет-0): ")))
