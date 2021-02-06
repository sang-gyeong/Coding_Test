# 동전 1

n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

d = [0 for _ in range(k + 1)]
d[0] = 1
for i in coin:
    for j in range(i, k + 1):
        d[j] += d[j - i]

print(d[k])
