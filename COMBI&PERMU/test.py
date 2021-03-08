from itertools import product

for i in product('가나다', 'ab'):
    print(''.join(list(i)), end=" ")
