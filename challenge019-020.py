from random import choice, sample, shuffle

s1 = input("Enter a studend #1: ")
s2 = input("Enter a studend #2: ")
s3 = input("Enter a studend #3: ")
s4 = input("Enter a studend #4: ")
student = [s1, s2, s3, s4]

# challenge 19
print("The chosen student is {}".format(choice(student)))
print("The two chosen students are {}".format(sample(student, 2)))

# challenge 20
shuffle(student)
print("The shuffled names are {}".format(student))