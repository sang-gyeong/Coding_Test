# 24분
# 키워드 : 조합

# 주어진 메뉴들을 course에 있는 숫자의 갯수별로 조합을 만든뒤, 몇번 등장하는지 세어 딕셔너리에 저장
# 딕셔너리를 순회하며 갯수별로 최대로 많이 호출된 메뉴조합을 result에 담은 뒤 정렬
# 튜플로 리턴된 combination을 문자열로 변환하는 코드 <= 다른 방법은 없는지 찾아보자


from itertools import combinations

def solution(orders, course):
    answer = []
    results = {}
    for order in orders:
        orderArr = sorted([a for a in order])
        for pickNum in course:
            combination = [ "".join(i) for i in combinations(orderArr, pickNum)]
            for c in combination:
                if c in results : results[c] += 1 
                else : results[c] = 1
    
    for pickNum in course:
        count = 2
        pickResult = []
        for result in results:
            if len(result) == pickNum and results[result] >= count :
                count = results[result]
                pickResult.append(result)
                pickResult = [p for p in pickResult if results[p] >= count]
        for p in pickResult:
            answer.append(p)
        
    answer.sort()
        
    return answer