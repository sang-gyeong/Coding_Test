from bisect import bisect_right


def solution(d, budget):
    d.sort()
    n = len(d)
    _d = [d[0]]
    for i in range(1, n):
        _d.append(_d[-1] + d[i])
    answer = bisect_right(_d, budget)

    return answer
