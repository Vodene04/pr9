def count_numbers():
    numbers = []
    even_count = 0
    odd_count = 0

    while True:
        user_inp = input("Введите число (или 'end' для завершения): ")

        if user_inp.lower() == 'end':
            break
        try:
            number = int(user_inp)
            numbers.append(number)
            if number % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        except ValueError:
            print("Ошибка ввода: введите корректное число или 'end'.")

    return even_count, odd_count

even, odd = count_numbers()
print(f"Четных чисел: {even}, Нечетных чисел: {odd}")