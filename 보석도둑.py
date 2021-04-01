import sys
import heapq

n, k = map(int, sys.stdin.readline().split())

a = []
bag = []
answer = 0

for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(a, [m, v])

for _ in range(k):
    c = int(sys.stdin.readline())
    heapq.heappush(bag, c)

bag.sort()
tmp = []

for space in bag:
    while len(a) > 0 and space >= a[0][0]:
        value = heapq.heappop(a)[1]
        heapq.heappush(tmp, -value)
    if len(tmp) > 0:
        answer -= heapq.heappop(tmp)
    elif len(a) == 0:
        break
print(answer)
