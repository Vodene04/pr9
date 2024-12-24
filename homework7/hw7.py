import random

def shift(numbers):

    last_element = numbers.pop()
    numbers.insert(0, last_element)

    return numbers

x = input('Введите длину списка: ')
try:
    x = int(x)

    numbers = [random.randint(1, 100) for _ in range(x)]

    print("Сгенерированный список:", numbers)

    shifted_numbers = shift(numbers)
    print("Список после сдвига:", shifted_numbers)
except ValueError:
    print('Неправильный ввод числа')