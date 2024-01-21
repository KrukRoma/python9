#1
try:
    name = input("Введіть своє ім'я: ")
    age = int(input("Введіть свій вік: "))
    if age < 0 or age > 130:
        raise ValueError("Ваш вік введено неправильно")
except ValueError as e:
    print(f"Помилка: {e}")
else:
    print(f"Привіт, {name}! Твій вік: {age}")

    

    