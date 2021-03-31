
# Challenge009 - Multiplication Table

num = int(input("Enter the number: "))
for i in range(1, 11):
    print("{} * {} = {}".format(num, i, num * i))