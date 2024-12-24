def squares(a, b):
    try:
        a = float(a)
        b = float(b)

        start = min(a, b)
        end = max(a, b)
        start = int (start)
        if end > int (end):
            end = int (end)
            squares = [i ** 2 for i in range(start + 1, end + 1)]
        else:
            end = int (end)
            squares = [i ** 2 for i in range(start + 1, end)]

        return squares
    except ValueError:
        return "Ошибка ввода: введите числовые значения."

a = input("Введите первое число: ")
b = input("Введите второе число: ")

result = squares(a, b)
print(result)