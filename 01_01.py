#Задание:
# Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительностиduration в секундах: до минуты: <s> сек;
# до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# для самостоятельного ввода раскоментировать 8 строку и законментировать 9 строку
#duration = int(input("Введите промежуток времени в секундах: "))
duration = 300
data = []
data.append(duration//86400)
data.append((duration-(data[0]*86400))//3600)
data.append((duration - (data[0] * 86400 + data[1]*3600)) // 60)
data.append(duration - (data[0] * 86400 + data[1] * 3600 + data[2]*60))

print("duration = ", duration)
if data[0] > 0:
    print(data[0], " дн", data[1], " час", data[2], " мин", data[3], " сек")
elif data[1] > 0:
    print(data[1], " час", data[2], " мин", data[3], " сек")
elif data[2] > 0:
    print(data[2], " мин", data[3], " сек")
elif data[3] > 0:
    print(data[3], " сек")
