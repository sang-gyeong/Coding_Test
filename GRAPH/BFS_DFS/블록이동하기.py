from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, x2, y2, n, graph):
    d = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append((x, y, x2, y2))
    while queue:
        x, y, x2, y2 = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= n:
                continue
            if graph[nx][ny] == 1 or graph[nx2][ny2] == 1:
                continue
            a, b = getFastDot(nx, ny, nx2, ny2)
            time = min(d[x][y], d[x2][y2])
            if (d[a][b]) == 0:
                d[nx][ny] = time + 1
                d[nx2][ny2] = time + 1
                queue.append((nx, ny, nx2, ny2))
        print(d)


def getFastDot(x, y, x2, y2):
    if (100-x)**2 + (100-y)**2 < (100-x2)**2 + (100-y2)**2:
        return x, y
    else:
        return x2, y2


def solution(board):
    n = len(board)
    bfs(0, 0, 0, 1, n, board)
