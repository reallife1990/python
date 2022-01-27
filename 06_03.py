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
        if i > length_h:
            data_dict[user.readline().replace('\n', '')] = None
        else:
            data_dict[user.readline().replace('\n', '')] = (hobby.readline().replace('\n', ''))

    print(data_dict)
with open('data.json', 'w', encoding='utf-8') as data_f:
    json.dump(data_dict, data_f, indent=4)
