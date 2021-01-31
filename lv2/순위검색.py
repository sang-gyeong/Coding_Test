def solution(info, query):
    answer = []
    
    for q in query:
        count = 0
        qArr = q.split()
        for i in info:
            iArr = i.split()
            if (iArr[0] == qArr[0] or qArr[0] == '-') and (iArr[1] == qArr[2] or qArr[2] == '-') and (iArr[2] == qArr[4] or qArr[4] == '-') and (iArr[3] == qArr[6] or qArr[6] == '-') and (int(iArr[4]) >= int(qArr[7])) :
                count += 1
        
        answer.append(count)
        
    return answer