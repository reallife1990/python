# Задание:
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 :
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых
# делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать
# в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму
# тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

numb = []

for i in range(1, 1001):
    if i % 2 == 1:
        numb.append(i ** 3)


def check_numbers():
    result = 0
    for number in numb:
        check_number = number
        result_check = 0
        while check_number >= 10:
            result_check += check_number % 10
            check_number = check_number // 10
        result_check += check_number
        if result_check % 7 == 0:
            result += number
    print(result)


print("сумма чисел из списка кубов делящихся на 7:")
check_numbers()
for i in range(len(numb)):
    numb[i] = numb[i] + 17

print("сумма чисел из изменённого списка кубов делящихся на 7:")
check_numbers()
