def solution(gems):
    answer = []
    count = 100000
    gemSet = set(gems)
    n = len(gemSet)
    start=0
    for end in range(1, len(gems)+1):
        now = set(gems[start:end])
        if len(set(now)) == n:
            while len(set(gems[start+1:end])) == n:
                start += 1
            gap = end-start+1
            if count > gap : 
                count = gap
                answer = [start+1, end]
            if n == gap:
                return answer
    
    return answer

from collections import deque

def solution2(gems):
    answer = []
    count = 100000
    gemSet = set(gems)
    n = len(gemSet)
    m = len(gems)
    end = 0
    now = deque()
    for start in range(m):
        while set(now) < gemSet and end < m:
            now.append(gems[end])
            end += 1
        if set(now) == gemSet:
            if count > end-start+1:
                count = end-start+1
                answer = [start+1, end]
        now.popleft()
    return answer