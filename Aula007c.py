n1 = int(input('first number: '))
n2 = int(input('second number: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2

print('the sum is {}, \nthe product is {}, \nthe division is {:.3f}'.format(s, m, d), end=' ')
print('the integer division is {}, the pow is {}'.format(di, p))
