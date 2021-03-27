from math import trunc, hypot, sin, cos, tan, degrees, radians

# challenge 16 - truncate
num1 = float(input("enter a float number: "))
print("int number is {}".format(trunc(num1)))

# challenge 17 - Pythagorean theorem
opLeg = float(input("type the opposite leg value: "))
adLeg = float(input("type the adjacent leg value: "))
print("The hypotenuse value is {:.2f}".format(hypot(opLeg, adLeg)))

# challenge 18 - sin, cos, tan (ps. All the trigonometric functions in Python assume that the input angle is in terms of radians )
angle = float(input("enter a angle value: "))
print("The Sine is {:.2f}, Cosine is {:.2f} and Tangent is {:.2f}".format(sin(radians(angle)), cos(radians(angle)), tan(radians(angle))))