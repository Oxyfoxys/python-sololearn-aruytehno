def welcome_to_python():
    """
1.1 Lesson
Welcome to Python!
    """
    print(welcome_to_python.__doc__)
    print("Welcome to Python!")


def your_first_program():
    """
1.2 Practice
Your First Program

Write a program to print "Python is fun".
Note that the sentence starts with a capital letter.

Hint
Use print() function.
    """
    print(your_first_program.__doc__)
    print("print: \"Python is fun\"")


def simple_operations():
    """
2.1 Lesson
Simple Operations
    """
    print(simple_operations.__doc__)
    print('2 + 2 =', 2 + 2)


def brain_freeze():
    """
2.2 Practice
Simple Operations


Today is a holiday at the children's camp, so all the children will be served ice cream.
There are 68 children in the group, and each child should get 2 scoops of ice cream.

Task
Write a program to calculate and output the total number of ice cream scoops we need.
    """
    print(brain_freeze.__doc__)
    print('#your code goes here')
    print('2 + 2 =', 2 + 2)


def floats():
    """
3.1 Lesson
Floats
    """

    print(floats.__doc__)
    print(3 / 4)
    print(0.42)


def exponentiation():
    """
4.1 Lesson
Exponentiation
    """

    print(floats.__doc__)
    print(2 ** 5)
    print(9 ** (1 / 2))


def quotient_and_remainder():
    """
5.1 Lesson
Quotient & Remainder
    """

    print(quotient_and_remainder.__doc__)
    print('20 // 6 =', 20 // 6)
    print('9 ** (1 / 2) =', 9 ** (1 / 2))
    print('20 % 6 =', 20 % 6)
    print('1.25 % 0.5 =', 1.25 % 0.5)


def quotient():
    """
5.2 Practice
Quotient

Calculate and output the number of miles in 1000 kilometers.

Hint
One mile is 1.6 kilometers, so find the quotient of 1000 and 1.6.
    """
    print(quotient.__doc__)
    print('#your code goes here')
    print('1000 // 1.6 =', 1000 // 1.6)


if __name__ == '__main__':
    # # 1.1
    # welcome_to_python()
    # # 1.2
    # your_first_program()
    # # 2.1
    # simple_operations()
    # # 2.2
    # brain_freeze()
    # # 3.1
    # floats()
    # # 4.1
    # exponentiation()
    # 5.1
    quotient_and_remainder()
    # 5.2
    quotient()
    # 6.1
