import sys
from writing import processing

elem = len(sys.argv)
file_u = ''
file_h = ''
if len(sys.argv) == 1:
    print('введите через пробел два входных адреса файлов в формате .csv \n '
          'и третий для выходных данных в формате .json \n'
          'Первый для пользователей, второй для хобби')
if len(sys.argv) == 4:
    for i in range(1, elem):
        if (3 > i >= 1 and (sys.argv[i][-4:]) == '.csv') or (i == 3 and (sys.argv[i][-5:]) == '.json'):
            print(f'Адрес "{sys.argv[i]}" принят')
        else:
            sys.exit(f'ошибка в адресе "{sys.argv[i]}".Выход.')
    print('Начинаем обработку...')
    module_ret = processing(sys.argv[1], sys.argv[2], sys.argv[3])
    if module_ret == 0:
        print("всё прошло успешно")
    else:
        print(f'внутренняя ошибка {module_ret}')
else:
    sys.exit('Неверное количество введеных адресов файлов')
