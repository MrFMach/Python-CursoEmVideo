import math
num1 = int(input("enter a int number"))
num2 = float(input("enter a float number"))
num3 = math.hypot(num1, num2)
print("the hypot between {} and {} is {}".format(num1, num2, num3))