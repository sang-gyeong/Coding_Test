from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    result = []
    n = len(banned_id)
    m = len(user_id)
    coms = list(permutations(user_id, len(banned_id)))
    for c in coms:
        isOk = True
        for i in range(n):
            if isMatch(banned_id[i], c[i])==False:
                isOk = False
                break
        if isOk == True :
            c = sorted(list(c))
            if not c in result:
                result.append(c)
    answer= len(result)
    return answer

def isMatch(banned, user):
    if len(banned) != len(user): return False
    for i in range(len(user)):
        if banned[i] != "*" and user[i] != banned[i]:
            return False
    return True