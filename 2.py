#2
def name_and_age(user_name, user_age):
    if user_age < 0 or user_age > 130:
        raise ValueError("Ваш вік введено неправильно")
    return f"Привіт, {user_name}! Твій вік : {user_age}"

try:
    user_name = input("Введіть своє ім'я : ")
    user_age = int(input("Введіть свій вік : "))
    result = name_and_age(user_name, user_age)
    print(result)
except ValueError as e:
    print(f"Помилка: {e}")