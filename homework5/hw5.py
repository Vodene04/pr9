import random

def big_numb (numbers):
    result = []
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            result.append(numbers[i])
    return result
x = input('Введите длину списка: ')
try:
    x = int(x)

    numbers = [random.randint(1, 100) for _ in range(x)]

    print("Сгенерированный список:", numbers)

    greater_elements = big_numb(numbers)
    print("Элементы, которые больше предыдущего:", greater_elements)
except ValueError:
    print('Неправильный ввод числа')