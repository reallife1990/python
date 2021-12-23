# Задание:
# Реализовать склонение слова «процент» во фразе «N процентов».

for i in range(1, 101):
    if i % 10 == 1 and i != 11:
        ending = ""
    elif (i % 10 == 2 or i % 10 == 3 or i % 10 == 4) and i//10 != 1:
        ending = "a"
    else:
        ending = "ов"
    print(i, "процент" + ending)

