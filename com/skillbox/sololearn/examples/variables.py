# https://www.tutorialspoint.com/python/python_variable_types.htm
counter = 100  # Целочисленное
miles = 1000.0  # С плавающей точкой
name = "John"  # Строка

print(counter)
print(miles)
print(name)

string = 'Hello World!'

print(string)  # Печатает строку
print(string[0])  # Печатает первый символ строки
print(string[2:5])  # Печатает символы строки, начиная с 3-го по 5-й.
print(string[2:])  # Выводит строку, начиная с 3-го символа
print(string * 2)  # Печатает строку два раза
print(string + "TEST")  # Конкатенация строк

# get type
user_id = "12tomsmith438"
print(type(user_id))  # <class 'str'>

user_id = 234
print(type(user_id))  # <class 'int'>

# Срезы
s = 'abcdefg'
print(s[1])
print(s[-1])
print(s[1:3])
print(s[1:-1])
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])
