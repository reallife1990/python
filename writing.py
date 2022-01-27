import json
def processing(file_1,file_2,file_out):
    data_dict = {}
    with open(file_1, 'r', encoding='utf-8') as user, \
         open(file_2, 'r', encoding='utf-8') as hobby:
        length_u = len(user.readlines())
        length_h = len(hobby.readlines())
        if length_u < length_h:
            return 1
        user.seek(0)
        hobby.seek(0)
        for i in range(0, length_u):
            fio = user.readline().replace('\n', '').split(',')
            hobby_lst = hobby.readline().replace('\n', '').split(',')
            if data_dict.get(fio[0]) is not None:
                data_dict[fio[0]] = [data_dict.get(fio[0]), [fio[1], fio[2], hobby_lst]]
            else:
                data_dict[fio[0]] = [fio[1], fio[2], hobby_lst]
    with open(file_out, 'w', encoding='utf-8') as data_f:
        json.dump(data_dict, data_f, indent=4)
    return 0


if __name__ == "__main__" :
    processing("users.csv", "hobby.csv", "fgh.json")
