from decimal import Decimal
import math

t = int(input())

for _ in range(t):
    answer = 'NO'
    x = int(input())
    for a in range(1, int(x/2)+1):
        rest = x-(a**3)
        if rest <= 0:
            break
        b = rest**(1.0/3.0)
        if abs(b - math.ceil(b)) <= 0.00000000001:
            answer = 'YES'
            break
    print(answer)
