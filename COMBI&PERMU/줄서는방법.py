from itertools import permutations


def solution(n, k):
    answer = []
    cases = permutations([i+1 for i in range(n)], n)
    answer = list(cases)[k-1]

    return answer
