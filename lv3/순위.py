def solution(n, results):
answer = 0
win = [[] for _ in range(n)]
lose = [[] for _ in range(n)]
hubo = [[i for i in range(1, n + 1)]for _ in range(n)]


for [a, b] in results:
    win[a - 1].append(b - 1)
lose[b - 1].append(a - 1)

print(win)
print(lose)
for i in range(n):
    win_count = len(win[i])
lose_count = len(lose[i])

hubo[i] = [h for h in hubo[i] if h > lose_count and h <= n - win_count]
for w in win[i]:
    if len(hubo[w]) > 0:
        hubo[i] = [h for h in hubo[i] if h < max(hubo[w])]
for w in lose[i]:
    if len(hubo[w]) > 0:
        hubo[i] = [h for h in hubo[i] if h > min(hubo[w])]

for h in hubo :
    if len(h) == 1:
        answer += 1

return answer