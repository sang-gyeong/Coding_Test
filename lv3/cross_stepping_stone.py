
## 정확도는 맞으나, 효율성에서 탈락함. (O^2)
def solution(stones, k):
    answer = 987654321
    m = 0
    b = 987654321
    for i in range(0, len(stones)-k+1):
        if stones[i+k-1] >= b : continue
        a = stones[i:i+k]
        m = max(a)
        b = max(m, b)
        answer = min(m, answer)
    print(b)
    return answer