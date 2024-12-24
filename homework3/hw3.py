def odd_numbers():
    numbers = []

    while True:
        user_input = input("Введите число (или 'end' для завершения): ")

        if user_input.lower() == 'end':
            break

        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Ошибка ввода: введите корректное число или 'end'.")

    odd_numbers = [num for num in numbers if num % 2 != 0]

    return odd_numbers

odd_list = odd_numbers()
print("Нечетные числа:", odd_list)