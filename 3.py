try:
    numbers = []
    input_str = input("Введіть список чисел через пробіл : ")
    input_numbers = [int(num) for num in input_str.split()]
    for number in input_numbers:
        if number <= 0:
            raise ValueError("Введено від'ємне чи нульове число.")
        numbers.append(number)
    sum1 = sum(numbers)
    print(f"Сума всіх додатніх чисел у списку : {sum1}")
except ValueError as e:
    print(f"Помилка: {e}")

