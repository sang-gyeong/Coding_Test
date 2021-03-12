from collections import deque

answer = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
a = []
isVisit = [[False]*m for _ in range(n)]

for _ in range(n):
    input_arr = list(map(int, input().split()))
    a.append(input_arr)

q = deque()
q.append((r, c, d))
while(q):
    (x, y, dir) = q.popleft()
    if isVisit[x][y] == False and a[x][y] == 0:
        isVisit[x][y] = True
        answer += 1
    for k in range(dir+7, dir+3, -1):
        k %= 4
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if isVisit[nx][ny] == False and a[nx][ny] == 0:
                q.append((nx, ny, k))
                break
        if k == dir:
            ax = x + dx[(dir+2) % 4]
            ay = y + dy[(dir+2) % 4]
            if a[ax][ay] == 0:
                q.append((ax, ay, dir))
            else:
                q.clear()
print(answer)
