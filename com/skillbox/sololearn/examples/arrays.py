"""
Dictionary (словарь)
https://metanit.com/python/tutorial/3.3.php
Особенность: Как и список, словарь хранит коллекцию элементов.
             Каждый элемент в словаре имеет уникальный ключ,
             с которым ассоциировано некоторое значение.
"""
print('============ Dictionary (словарь) ============')
users = {1: "Tom", 2: "Bob", 3: "Bill"}

elements = {"Au": "Золото", "Fe": "Железо", "H": "Водород", "O": "Кислород"}

print(users[1])

"""
List (список)
https://metanit.com/python/tutorial/3.1.php
Особенность: хранит тип данных, который хранит набор или последовательность элементов
"""
print('============ List (список) ============')
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # 1
print(numbers[2])  # 3
print(numbers[-3])  # 3

numbers[0] = 125  # изменяем первый элемент списка
print(numbers[0])  # 125

"""
Set (множество)
https://metanit.com/python/tutorial/3.4.php
Особенность: множество содержит только уникальные значения.
"""
print('============ Set (множество) ============')
users = {"Tom", "Bob", "Alice", "Tom"}
print(users)  # {"Tom","Bob","Alice"}

"""
Tuple (кортеж)
https://metanit.com/python/tutorial/3.2.php
Особенность: является неизменяемым (immutable) типом
"""
print('============ Tuple (кортеж) ============')
print("")
user = ("Tom", 23)
print(user)

# list -> tuple
users_list = ["Tom", "Bob", "Kate"]
users_tuple = tuple(users_list)
print(users_tuple)  # ("Tom", "Bob", "Kate")
# users_tuple[1] = "Tim" # TypeError: 'tuple' object does not support item assignment

# split tuple
user = ("Tom", 22, False)
name, age, isMarried = user
print(name)  # Tom
print(age)  # 22
print(isMarried)  # False


def get_user():
    name = "Tom"
    age = 22
    is_married = False
    return name, age, is_married


# return tuple
user = get_user()
print(user[0])  # Tom
print(user[1])  # 22
print(user[2])  # False

# user = ("Tom", 22, False)
print(len(user))  # 3
