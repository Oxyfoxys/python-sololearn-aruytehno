def welcome_to_python():
    """
1.1 Lesson
Welcome to Python!
    """
    print(welcome_to_python.__doc__)
    print('print:', 'Welcome to Python!')


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
    print('print:', 'Python is fun')


def simple_operations():
    """
2.1 Lesson
Simple Operations
    """
    print(simple_operations.__doc__)
    print('2 + 2 =', 2 + 2)
    print('1 + 2 + 3 =', 1 + 2 + 3)
    print('2 * (3 + 4) =', 2 * (3 + 4))
    print('5 + 4 - 3 =', 5 + 4 - 3)


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
    print('68 * 2 =', 68 * 2)


def floats():
    """
3.1 Lesson
Floats
    """

    print(floats.__doc__)
    print('print:', 0.42)
    print('3 / 4 =', 3 / 4)
    print('3 / 4 =', 8 / 2)
    print('7 * 7.0 =', 7 * 7.0)
    print('4 * 1.65 =', 4 * 1.65)
    print('1 + 2 + 3 + 4.0 + 5 =', 1 + 2 + 3 + 4.0 + 5)


def exponentiation():
    """
4.1 Lesson
Exponentiation
    """

    print(exponentiation.__doc__)
    print('2 ** 5 =', 2 ** 5)
    print('2 ** 3 ** 2 =', 2 ** 3 ** 2)
    print('9 ** (1 / 2) =', 9 ** (1 / 2))


def quotient_and_remainder():
    """
5.1 Lesson
Quotient & Remainder
    """

    print(quotient_and_remainder.__doc__)
    print('20 // 6 =', 20 // 6)
    print('20 % 6 =', 20 % 6)
    print('1.25 % 0.5 =', 1.25 % 0.5)
    print('7 % (5 // 2)', 7 % (5 // 2))


def how_many_miles():
    """
5.2 Practice
Quotient

Calculate and output the number of miles in 1000 kilometers.

Hint
One mile is 1.6 kilometers, so find the quotient of 1000 and 1.6.
    """
    print(how_many_miles.__doc__)
    print('#your code goes here')
    print('1000 // 1.6 =', 1000 // 1.6)


def module_1_quiz():
    """
6.1 Lesson
Module 1 Quiz
    """
    print(module_1_quiz.__doc__)
    print('1 + 4 * 3 =', 1 + 4 * 3)
    print('print:', 'I love Python')
    print('(3 ** 2) // 2 =', (3 ** 2) // 2)
    print('100 // 42', 100 // 42)
    print('10 ** 5 =', 10 ** 5)


def code_project_exponentiation():
    """
7 Code project
Exponentiation

Exponentiation is the raising of one number to the power of another.
This operation is performed using two asterisks **.

Let's use exponentiation to solve a known problem.
You are offered a choice of either $1.000.000 or $0.01 (one penny) doubled every day for 30 days (the resulting amount
is doubled every day).

Task:
Write a program to calculate the amount that will result from the doubling to understand which choice results in a
larger amount.

Hint:
Let's see how exponentiation can be useful to perform the calculation.
For example, if we want to calculate how much money we will have on the 5th day, we can use this expression: 0.01*(2**5)
= 0.32 dollars (multiply the penny by 2 raised to the power of 5).
    """
    print(code_project_exponentiation.__doc__)
    print('#your code goes here')
    print('0.01 * (2 ** 30) =', 0.01 * (2 ** 30))


if __name__ == '__main__':
    # 1.1
    welcome_to_python()
    # 1.2
    your_first_program()
    # 2.1
    simple_operations()
    # 2.2
    brain_freeze()
    # 3.1
    floats()
    # 4.1
    exponentiation()
    # 5.1
    quotient_and_remainder()
    # 5.2
    how_many_miles()
    # 6.1
    module_1_quiz()
    # 7 Code project
    code_project_exponentiation()
