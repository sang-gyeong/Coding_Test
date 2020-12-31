# 미로탐색 (BFS)

from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while len(queue) > 0:
    x, y = queue.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  return graph[n-1][m-1]

print(bfs(0, 0))

