# coding=utf-8
coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input("Select 1-5: "))
try:
    print(coffee[choice - 1])
except:
    print("Invalid number")
finally:
    print("Have a good day")
