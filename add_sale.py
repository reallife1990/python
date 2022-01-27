import sys
if len(sys.argv) == 2:
    text = str(sys.argv[1] + ' ' * (15-(len(sys.argv[1]))))
    print(len(text))
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        print(f.tell())
        f.write(f'{text}\n')
