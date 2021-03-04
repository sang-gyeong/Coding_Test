def solution(numbers, hand):
    answer = ''
    position = [[3,1], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
    leftArr = [1, 4, 7]
    rightArr = [3, 6, 9]
    middleArr = [2,5,8,0]
    left = [3, 0]
    right = [3, 2]
    
    for num in numbers:
        target = position[num]
        if num in leftArr:
            left = target
            answer+="L"
        elif num in rightArr:
            right = target
            answer += "R"
        elif num in middleArr:
            if getDistance(target, left) < getDistance(target, right):
                left = target
                answer+="L"
            elif getDistance(target, left) > getDistance(target, right): 
                right = target
                answer += "R"
            elif getDistance(target, left) == getDistance(target, right): 
                if hand=="right":
                    right = target
                    answer += "R"
                else:
                    left = target
                    answer+="L"
    
    return answer

def getDistance(target, hand):
    [x, y] = target
    [x2, y2] = hand
    return abs(x-x2) + abs(y-y2)