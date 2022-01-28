import os.path

ROOT_DIR = './test_dir'


def count(num, res):
    if limit[num] < res < limit[num + 1]:
        a = val[num]
        a += 1
        val[num] = a
        if type(file_ext[num]) is list:
            lst_tmp = file_ext[num]
        else:
            lst_tmp = []
        lst_tmp.append(f.split('.')[1])
        file_ext[num] = lst_tmp


limit = [0, 100, 1000, 10000, 100000, 1000000]
val = [0, 0, 0, 0]
file_ext = ['', '', '', '']
for root, _, files in os.walk(ROOT_DIR):
    for f in files:
        for i in range(len(limit) - 2):
            count(i, os.stat(os.path.realpath(f'{root}/{f}'))[6])

for i in range(len(file_ext)):
    file_ext[i] = list(set(file_ext[i]))
limit.remove(0)
d = dict(zip(limit, list(zip(val, file_ext))))
print(d)
