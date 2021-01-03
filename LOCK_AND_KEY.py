import copy

def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    v_lock = [[0] * (n+(m-1)*2) for _ in range(n+(m-1)*2)]
    for i in range(n):
        for j in range(n):
            v_lock[i+(m-1)][j+(m-1)] = lock[i][j]
    test_lock = copy.deepcopy(v_lock)
    for i in range(n+m-1):
        for j in range(n+m-1):
            for _ in range(4):
                key = rotate90(key)
                for k in range(m):
                    for l in range(m):
                        test_lock[i+k][j+l] += key[k][l]
                if isFit(test_lock, n, m): return True
                else: test_lock = copy.deepcopy(v_lock)
    return answer

def rotate90(key):
    m = len(key)
    ret = [[0] * m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            ret[c][m-1-r] = key[r][c]
    return ret

def isFit(test_lock, n, m):
    for i in range(n):
        for j in range(n):
            if test_lock[i+(m-1)][j+(m-1)] != 1: return False
    return True
    