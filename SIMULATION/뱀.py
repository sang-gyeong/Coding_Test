from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
k = int(input())

apples = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    apples[x-1][y-1] = 1

l = int(input())
changes = {}
for _ in range(l):
    sec, new_dir = map(str, input().split())
    changes[int(sec)] = new_dir

spaces = deque()
spaces.appendleft([0, 0])

x, y = 0, 0
dir = 1
sec = 0
while(True):
    # 초 증가 및 이동좌표 찍기
    sec += 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 벽을 부딪힐 경우
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break

    # 사과를 먹음
    if apples[nx][ny] == 1:
        apples[nx][ny] = 0
    else:
        if (spaces):
            spaces.pop()
     # 자기 몸통과 부딪힐 경우
    if [nx, ny] in spaces:
        break

    spaces.appendleft([nx, ny])
    # 방향 바꾸기
    if sec in changes:
        new_dir = changes[sec]
        if new_dir == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
    x = nx
    y = ny

print(sec)
