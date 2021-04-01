import sys

n = int(sys.stdin.readline())
mod = 1000000000
global answer
answer = 0


def go(idx, n, prev, left_nums):
    global answer
    if n - idx < len(left_nums):
        return
    if idx == n:
        if len(left_nums) == 0:
            answer = (answer + 1) % mod
        return
    for num in range(0, 10):
        if num == prev + 1 or num == prev - 1:
            go(idx + 1, n, num,
               [i for i in left_nums if i != num])
    return


for i in range(1, 10):
    go(1, n, i, [j for j in range(0, 10) if j != i])

print(answer)
