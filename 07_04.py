import os.path

ROOT_DIR = './test_dir'
res = {100: 0, 1000: 0, 10000: 0, 100000: 0}

for root, _, files in os.walk(ROOT_DIR):
    for f in files:
        print(f.split('.')[1])
        result = (os.stat(os.path.realpath(f'{root}/{f}'))[6]//100)
        if result < 1:
            a = res.get(100)
            a += 1
            res[100] = a
            print(res.get(100))
        elif result < 10:
            a = res.get(1000)
            a += 1
            res[1000] = a
            print(res.get(1000))
        elif result < 100:
            a = res.get(10000)
            a += 1
            res[10000] = a
            print(res.get(10000))
        elif result < 1000:
            a = res.get(100000)
            a += 1
            res[100000] = a
            print(res.get(100000))
print(res)
