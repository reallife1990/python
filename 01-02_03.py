def num_translate(key):
    """ Translate numbers """
    if key.islower():
        print(numbers_text.get(key))
    else:
        print(numbers_text.get(key.lower()).capitalize())


numbers_text = {"один": "one", "два": "two",
                "три": "three", "четыре": "four",
                "пять": "five", "шесть": "six",
                "семь": "seven", "восемь": "eight",
                "девять": "nine", "ноль": "zero",
                "one": "один", "two": "два",
                "three": "три", "four": "четыре",
                "five": "пять", "six": "шесть",
                "seven": "семь", "eight": "восемь",
                "nine": "девять", "zero": "ноль",
                "ten": "десять", "десять": "ten"}


num_translate(input("Введите число от 0 до 10 на английском или русском языке прописью: "))