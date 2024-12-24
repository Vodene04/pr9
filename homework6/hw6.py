import random

def swap(numbers):

    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))

    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

    return numbers

x = input('Введите длину списка: ')
try:
    x = int(x)

    numbers = [random.randint(1, 100) for _ in range(x)]

    print("Сгенерированный список:", numbers)

    swapped_numbers = swap(numbers)
    print("Список после замены:", swapped_numbers)
except ValueError:
    print('Неправильный ввод числа')