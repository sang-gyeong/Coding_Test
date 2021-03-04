from collections import deque

def solution(gems):
    answer = []
    count = 100000
    n = len(set(gems))
    gem_dict = dict()
    end = 0
    for start in range(len(gems)):
        while len(gem_dict) < n and end < len(gems):
            if gem_dict.get(gems[end]) is None : gem_dict[gems[end]] = 1
            else : gem_dict[gems[end]] += 1
            end += 1
        if len(gem_dict) == n:
            if count > end-start+1:
                count = end-start+1
                answer = [start+1, end]
        gem_dict[gems[start]] -= 1
        if gem_dict[gems[start]] == 0 : del gem_dict[gems[start]]
    return answer


# 효율성에서 시간초과가 났던 코드

# from collections import deque
# def solution(gems):
#    answer = []
#    count = 100000
#    gemSet = set(gems)
#    n = len(gemSet)
#    m = len(gems)
#    end = 0
#    now = deque()
#    for start in range(m):
#        while set(now) < gemSet and end < m:
#            now.append(gems[end])
#            end += 1
#        if set(now) == gemSet:
#            if count > end-start+1:
#                count = end-start+1
#                answer = [start+1, end]
#        now.popleft()
#    return answer