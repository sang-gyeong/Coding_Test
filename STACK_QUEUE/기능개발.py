import math


def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    left_days = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(n)]
    max_day = left_days[0]
    count = 0
    for day in left_days:
        if day > max_day:
            max_day = day
            answer.append(count)
            count = 1
        else:
            count += 1
    answer.append(count)
    return answer
