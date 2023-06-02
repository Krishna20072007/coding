from math import factorial
from decimal import *

getcontext().prec = 10000000000

e = 1
end = 10000000

for x in range(1, end):
    term = Decimal(1/(factorial(x)))
    e += term

print(e)

