from itertools import product

answer = 0
n, k = map(int, input().split())
a = [i for i in range(n + 1)]
permutation = product(a, repeat=k)

for p in permutation:
    print(p)
    if sum(p) == n:
        answer += 1

print(answer % 1000000000)


# n, k = map(int, input().split())
# a = [[0] * k for _ in range(n + 1)]

# for i in range(k):
#     a[0][i] = 1

# for i in range(n + 1):
#     a[i][1] = 1


# for i in range(1, n+1):
#     for j in range(1, k+1):
#         a[i][j] = a[i-1][j-1]


# print(a)
