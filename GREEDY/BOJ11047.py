# 동전 0 (그리디)

n, k = map(int, input().split())

answer = 0
coinArr = []
for _ in range(n):
  coinArr.append(int(input()))

coinArr.sort(reverse = True)
for coin in coinArr:
  if coin <= k:
    count = k//coin
    answer = answer + count
    k = k-(count*coin)
print(answer)