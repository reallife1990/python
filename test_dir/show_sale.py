import sys

def readind(start =0 ,ending=None):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(start)
        print(ending)
        f.seek(start)
        print(f.read(ending))


if len(list(sys.argv)) == 1:
    readind()
if len(list(sys.argv)) == 2:
    readind(15*(int(sys.argv[1])-1))
if len(list(sys.argv)) == 3:
    readind(17*(int(sys.argv[1])-1), 16*(int(sys.argv[2])-int(sys.argv[1])+1))

