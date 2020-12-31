# 수들의 합 (투 포인터)

n, m = map(int, input().split())
a = list(map(int, input().split()))

result = 0
end = 0
sum = 0
for start in range(n):
    while sum < m and end < n:
        sum += a[end]
        end += 1
    if sum == m:
        result += 1
    sum -= a[start]
print(result)



