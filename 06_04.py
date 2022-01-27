import sys
import json
data_dict = {}
with open('users.csv', 'r', encoding='utf-8') as user, \
     open('hobby.csv', 'r', encoding='utf-8') as hobby:
    length_u = len(user.readlines())
    length_h = len(hobby.readlines())
    if length_u < len(hobby.readlines()):
        sys.exit(1)
    user.seek(0)
    hobby.seek(0)
    for i in range(0, length_u):
        fio = user.readline().replace('\n', '').split(',')
        hobby_lst = hobby.readline().replace('\n', '').split(',')
        if data_dict.get(fio[0]) is not None:
            data_dict[fio[0]] = [data_dict.get(fio[0]), [fio[1], fio[2], hobby_lst]]
        else:
            data_dict[fio[0]] = [fio[1], fio[2], hobby_lst]
    print(data_dict)

with open('data2.json', 'w', encoding='utf-8') as data_f:
    json.dump(data_dict, data_f, indent=4)
