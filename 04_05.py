src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [elem for elem in src[1:] if elem > src[src.index(elem)-1]]
print(result)
