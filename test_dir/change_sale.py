import sys


def readind(start, content):
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        f.seek(start)
        f.write(f'{content}\n')


ln_t = len(list(sys.argv))
if len(list(sys.argv)) == 3:
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        size = f.tell()
        print(size)
        if size <= (17*(int(sys.argv[1])-1)):
            print(f'такой строки не существует, максимальная №{int(size/17)}')
        else:
            readind(17*(int(sys.argv[1])-1), str(sys.argv[2] + ' ' * (15-(len(sys.argv[2])))))