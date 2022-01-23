tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '10В', '10Б']


def h():
    for elem in tutors:
        elem1 = None
        if tutors.index(elem) < len(klasses):
            elem1 = klasses[tutors.index(elem)]
        yield elem, elem1


s = h()
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
