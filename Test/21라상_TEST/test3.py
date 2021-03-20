# 배열 두개가 주어졌을때 확실히 만난 애들 만난 사람 명수 순서대로 배열에 담아서 리턴하기

from itertools import combinations


def solution(enter, leave):
    n = len(leave)
    answer = []
    result = {}
    count = [0] * (n+1)
    for i in range(n):
        target = leave[i]
        start = enter.index(target)
        if i == 0:
            result[target] = [start, start+1]
            continue
        prev_end = result[leave[i-1]][1]
        if start + 1 < prev_end:
            result[target] = [start, prev_end]
        else:
            result[target] = [start, start+1]

    cases = combinations([i for i in range(1, n+1)], 2)
    for case in cases:
        (i, j) = case
        [a, b] = result[i]
        [c, d] = result[j]
        if (c < a and a < d) or (a < c and c < b) or (c < a and b <= d) or (a < c and d <= b):
            count[i] += 1
            count[j] += 1

    answer = count[1:]
    return answer
