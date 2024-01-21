def sum_of_numbers(numbers):
    if any(num <= 0 for num in numbers):
        raise ValueError("Введено від'ємне чи нульове число.")
    return sum(numbers)
try:
    input_str = input("Введіть список чисел через пробіл: ")
    input_numbers = [int(num) for num in input_str.split()]
    result = sum_of_numbers(input_numbers)
    print(f"Сума всіх додатніх чисел у списку: {result}")
except ValueError as e:
    print(f"Помилка: {e}")

