
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


# 이진탐색 기법을 사용하여 효율성 테스트 통과
def solution2(stones, k):
    start = 0
    end = 200000000 # max(stones) 라고 하니 오류 발생
    
    while(start < end-1):
        mid = (start + end) // 2
        if isOk(stones, mid, k)==True:
            start = mid
        else :
            end = mid
    return start

def isOk(arr, mid, k):
    count = 0
    for a in arr:
        if a < mid:
            count += 1
        else:
            count = 0
        if count >= k : return False
    return True