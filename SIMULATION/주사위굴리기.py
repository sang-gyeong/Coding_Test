import copy

n, m, x, y, k = map(int, input().split())

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


dice = [0]*6
maps = []
for _ in range(n):
    input_arr = list(map(int, input().split()))
    maps.append(input_arr)


def rotateDice(arr, dir):
    _arr = copy.deepcopy(arr)
    if dir == 1:
        _arr[0] = arr[3]
        _arr[2] = arr[0]
        _arr[3] = arr[5]
        _arr[5] = arr[2]
    elif dir == 2:
        _arr[0] = arr[2]
        _arr[2] = arr[5]
        _arr[3] = arr[0]
        _arr[5] = arr[3]
    elif dir == 3:
        _arr[0] = arr[4]
        _arr[1] = arr[0]
        _arr[4] = arr[5]
        _arr[5] = arr[1]
    elif dir == 4:
        _arr[0] = arr[1]
        _arr[1] = arr[5]
        _arr[4] = arr[0]
        _arr[5] = arr[4]
    return _arr


orders = list(map(int, input().split()))
for o in orders:
    nx = x + dx[o]
    ny = y + dy[o]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    dice = rotateDice(dice, o)
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[5]
    else:
        dice[5] = maps[nx][ny]
        maps[nx][ny] = 0

    print(dice[0])
    x = nx
    y = ny
