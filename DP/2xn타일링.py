# 2xn 타일링
n = int(input())

d = [0, 1, 3]

for i in range(3, n + 1):
    d.append((d[i - 1] + (d[i - 2] * 2)) % 10007)

print(d[n])
