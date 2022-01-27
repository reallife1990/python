with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    length = len(f.readlines())
    f.seek(0)
    result = []
    for i in range(0, length):
        data = f.readline()
        elem_t = (data.split(' ')[0], data.split(' ')[5][1:], data.split(' ')[6])
        result.append(elem_t)

    print(result)



