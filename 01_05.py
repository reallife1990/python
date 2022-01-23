

def f_gen(out):
    for i in range(1, out+1, 2):
        yield i


num_gen = f_gen(15)
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
