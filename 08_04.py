def checker(callback):
    def _checker(func):
        def wrapper(*args):
            for i in args:
                if callback(i) is True:
                    print(i)
                    result = func(i)
                else:
                    raise ValueError(f'wrong value {i}')
            return result
        return wrapper
    return _checker


@checker(lambda x : int(x) > 0)
def calc_cube(x):
    return print(x**3)


a = calc_cube(3)


