import os
import json


def cr_file(name, way="./"):
    #print(str(way)+str(name))
    with open(str(way)+str(name), 'w', encoding='utf-8') as q:
        pass
        #print(f"{name}, {way}")


def cr_dir(lst_dir, way="", acc="./"):
     names = acc+way
     #print(names)
     for i in lst_dir.keys():
        if names != i:
            names =(f'{way}{i}')
        #way=(f'{way}{i}')
        print(f'way:{names}')

        if not os.path.exists(way + i): # создать папку
            os.mkdir(way + i)
        #print(type(lst_dir.get(i)))
        if type(lst_dir.get(i)) is dict: # если словарь, закидываем вновь
            print(f"{i}-dict")
            cr_dir(lst_dir.get(i), f"{i}/")
            print(lst_dir.get(i))
        if type(lst_dir.get(i)) is list: # если список,перебираем
            for i_lst in lst_dir.get(i):
                print(type(i_lst), i_lst)
                if type(i_lst) is str:
                    print(f"{i}")
                    cr_file(i_lst, f"{names}/")
                if type(i_lst) is dict:
                    cr_dir(i_lst, f"{names}")
                    print(f"{i_lst}")
                    print(i_lst.keys())

        if not os.path.exists(way+i):
            os.mkdir(way+i)


with open('config.json', 'r', encoding="utf-8") as conf:
    a = json.loads(conf.read())
if type(a) is dict:
    names = ''
    cr_dir(a)
print(type(a))
print(list(a.keys()))
"""
for k in a.keys():
    k1 = (a.get(k))
    #print(type(k))
    #print(k1.keys())
    #print(f'1+{k1}')
    for y in k1.keys():
        t = (k1.get(y))
        for item in t:
            #print(type(item))
            if type(item) is str:
                print(item)
                #pass # ccreate files
            if type(item) is dict:
                print(f'словарь{item}')
                for x in item.keys():
                    print(x)
                    t1 = (item.get(x))
                    print(t1)
                    print(type(t1))"""



