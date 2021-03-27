from math import sqrt, ceil, floor, hypot  ## import just library modules
import random   ## import full library

randomRange = random.randrange(150, 300, 3)  ## random start, stop, step
print("Random number: {}".format(randomRange))

sqRoot = sqrt(randomRange)
print('The {} square root is {}'.format(randomRange, sqRoot))
print('The {} square root is {:.2f}, two decimal'.format(randomRange, sqRoot))
print('The {} square root is {}, round up'.format(randomRange, ceil(sqRoot)))
print('The {} square root is {}, round down'.format(randomRange, floor(sqRoot)))

catx = 8
caty = sqRoot
print('The hypotenuse of {} and {} is {} '.format(catx, caty, hypot(catx, caty)))