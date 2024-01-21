def sum_of_numbers(numbers):
    try:
        if any(num <= 0 for num in numbers):
            raise ValueError("Введено від'ємне чи нульове число.")
        return sum(numbers)
    except ValueError as e:
        raise e

try:
    input_str = input("Введіть список чисел через пробіл: ")
    input_numbers = [int(num) for num in input_str.split()]
    result = sum_of_numbers(input_numbers)

    if result is not None:
        print(f"Сума всіх додатніх чисел у списку: {result}")

except ValueError as e:
    print(f"Помилка: {e}")



