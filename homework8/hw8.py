import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]


def user_selection():
    user_numbers = []
    for i, row in enumerate(ticket):
        while True:
            try:
                user_input = int(input(f"Выберите число из строки {i + 1} {row}: "))
                if user_input in row:
                    user_numbers.append(user_input)
                    break
                else:
                    print("Ошибка: число должно быть в указанной строке.")
            except ValueError:
                print("Ошибка: введите корректное число.")
    return user_numbers


def random_selection():
    pc_numbers = [random.choice(row) for row in ticket]
    return pc_numbers


def display_results(user_numbers, pc_numbers):
    print("\nВаши выбранные числа:", user_numbers)
    print("Случайно выбранные числа ПК:", pc_numbers)

    matches = set(user_numbers) & set(pc_numbers)
    print(f"Количество совпадений: {len(matches)}")
    print("Совпадающие числа:", matches)


user_numbers = user_selection()
pc_numbers = random_selection()
display_results(user_numbers, pc_numbers)