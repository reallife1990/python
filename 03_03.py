# Написать функцию thesaurus(), принимающую в качестве аргументов
# имена сотрудников и возвращающую словарь, в котором ключи —
# первые буквы имён, а значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.


def thesaurus(*args):
    for i in args:
        k = i[0]
        if d.get(k) is None:
            temp_lst = [i]

        else:
            temp_lst = d.get(k)
            temp_lst.append(i)
        d[k] = temp_lst


d = {}

thesaurus("Иван", "Мария", "Петр", "Илья", "Павел")
print(d)
