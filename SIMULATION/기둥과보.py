def solution(n, build_frame):
    answer = []
    poll = []
    bottom = []
    for order in build_frame:
        canRemove = True
        [x, y, isBottom, isBuild] = order
        if isBuild :
            if isBottom:
                if checkBottom(x, y, poll, bottom):
                    bottom.append([x,y])
            else:
                if checkPoll(x, y, poll, bottom):
                    poll.append([x,y])
        else :
            bottom.remove([x, y]) if isBottom else poll.remove([x,y])
            for p in poll:
                if not checkPoll(p[0], p[1], poll, bottom) :
                    canRemove = False
                    break
            for b in bottom:
                if not checkBottom(b[0], b[1], poll, bottom) :
                    canRemove = False
                    break
            if canRemove==False : 
                bottom.append([x, y]) if isBottom else poll.append([x,y])
    for p in poll:
        answer.append([p[0], p[1], 0])
    for b in bottom:
        answer.append([b[0], b[1], 1])
    answer = sorted(answer, key=lambda x : (x[0], x[1], x[2]))        
    return answer

def checkPoll(x, y, poll, bottom):
    if y==0 or [x,y] in bottom or [x-1, y] in bottom or [x, y-1] in poll:
        return True
    return False

def checkBottom(x, y, poll, bottom):
    if [x, y-1] in poll or [x+1, y-1] in poll or ([x-1, y] in bottom and [x+1, y] in bottom):
        return True
    return False