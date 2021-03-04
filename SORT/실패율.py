# 21분 소요

# 1. for문을 통해 스테이지 수만큼 분모, 분자를 넣음
# 2. 실패율을 계산 후, 튜플 형태로(i, 실패율(result)) 저장
# 3. result를 기준으로 내림차순 정렬

def solution(N, stages):
    answer = []
    resultArr = []
    numArr = [0]*(N+2)
    denArr = [0]*(N+2)
    for stage in stages:
      numArr[stage] = numArr[stage] + 1
      for i in range(stage+1) :
        denArr[i] = denArr[i]+1

    for i in range(1, N+1):
      if denArr[i] == 0:
        result = 0
      else :
        result = numArr[i] / denArr[i]
      resultArr.append((i, result))
    sortedArr = sorted(resultArr, key = lambda x : x[1], reverse=True)
    for tuple in sortedArr :
      answer.append(tuple[0])
    return answer