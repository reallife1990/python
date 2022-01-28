price = [57.8, 46.51, 97, 115.1, 58, 183.15, 14.7, 79.5, 88.4, 15, 99.99, 40, 59.26, 150, 58.44, 96.7, 230.14, 25.18,
         20, 36.82]
for i in price:
    if i == price:
        rub = int(i)
        kop = int((i*100) - (rub*100))
        print(f'{rub} руб {kop:02d} коп' , end = '.\n')
    else:
        rub = int(i)
        kop = int((i*100) - (rub*100))
        print(f'{rub} руб {kop:02d} коп', end = ',')
# print(list2)