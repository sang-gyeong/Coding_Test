
import sys

n = int(sys.stdin.readline())

check_col = [False] * n
check_dig = [False] * (2 * n + 1)
check_dig2 = [False] * (2 * n + 1)


def check(row, col):
    if (check_col[col]):
        return False
    if (check_dig[row+col]):
        return False
    if (check_dig2[row-col+n-1]):
        return False
    return True


def calc(row):
    if row == n:
        return 1
    cnt = 0
    for col in range(0, n):
        if check(row, col):
            check_dig[row + col] = True
            check_dig2[row-col+n-1] = True
            check_col[col] = True
            cnt += calc(row + 1)
            check_dig[row + col] = False
            check_dig2[row-col+n-1] = False
            check_col[col] = False
    return cnt


print(calc(0))
