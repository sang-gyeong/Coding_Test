# RGB거리

n = int(input())
a = [[0] * 3 for i in range(n)]
d = [[0] * 3 for i in range(n)]

for i in range(n):
    a[i][0], a[i][1], a[i][2] = map(int, input().split())

d[0] = a[0]

for i in range(1, n):
    d[i][0] = a[i][0] + min(d[i - 1][1], d[i - 1][2])
    d[i][1] = a[i][1] + min(d[i - 1][0], d[i - 1][2])
    d[i][2] = a[i][2] + min(d[i - 1][0], d[i - 1][1])

print(min(min(d[n - 1][0], d[n - 1][1]), d[n - 1][2]))
