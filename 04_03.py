# (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи
# — первые буквы фамилий, а значения — словари, реализованные
# по схеме предыдущего задания и содержащие записи, в которых
# фамилия начинается с соответствующей буквы.
def thesaurus_adv(*args):
    """
    :param args:  name and surname
    :return: sorted dictionary
    """
    tmp = []
    for i in args:
        tmp.append(i)
    tmp.sort(key=lambda let_s: let_s[i.index(" ")+1])
    
    for el in tmp:
        surname = el[el.index(" ")+1]
        res = {}
        if d1.get(surname) is None:
            d1[surname] = thesaurus(el, res)
        else:
            d1[surname] = thesaurus(el, d1[surname])


def thesaurus(io, tmp_dict):
    """
    :param io:  element into arguments
    :param tmp_dict:  temporary dictionary
    :return: finished dictionary with sorted elements
    """
    k = io[0]
    if tmp_dict.get(k) is None:
        temp_lst = [io]
    else:
        temp_lst = tmp_dict.get(k)
        temp_lst.append(io)
        temp_lst.sort(key=lambda let_n: let_n[0])
    tmp_dict[k] = temp_lst
    return tmp_dict


d1 = {}
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(d1)
