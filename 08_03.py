def decorator(func):
    def wrapper(*args):
        lst_result = []
        for i in args:
            result = func(i)
            lst_result.append(f'{i}:{type(i)}')
        print(lst_result)
        return result
    return wrapper


@decorator
def calc_cube(val):
    return val**3


a=(calc_cube(10,258,852,5623))
