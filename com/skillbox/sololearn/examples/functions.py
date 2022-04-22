def main():
    say_hello()
    say_hello()
    say_hello()

    result1 = exchange(60, 30000)
    print(result1)
    result2 = exchange(56, 30000)
    print(result2)
    result3 = exchange(65, 30000)
    print(result3)

    user_name, user_age = create_default_user()
    print("Name:", user_name, "\t Age:", user_age)


def say_hello():
    print("Hello")


def exchange(usd_rate, money):
    result = round(money / usd_rate, 2)
    return result


def create_default_user():
    name = "Tom"
    age = 33
    return name, age


# Вызов функции main
main()
