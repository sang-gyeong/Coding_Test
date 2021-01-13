def solution(lines):
    answer = 0
    start = []
    end = []
    for log in lines:
        [date, time, gapSec] = log.split()
        [hour, min, sec] = time.split(':')
        gap = int(float(gapSec[:-1]) * 1000)
        endTime = int(hour) * 3600000 + int(min) * 60000 + int(float(sec)*1000)
        startTime = endTime - gap + 1
        start.append(startTime)
        end.append(endTime)
    for i in range(len(start)):
        count = 0
        fromTime = start[i]
        toTime = start[i] + 999
        for j in range(len(start)):
            if (end[j] >= fromTime and start[j] <= fromTime) or (start[j] >= fromTime and end[j] <= toTime) or (start[j] <= toTime and end[j] >= toTime) or (start[j] <= fromTime and end[j] >= toTime):
                count +=1
        answer = max(answer, count)
    for i in range(len(end)):
        count = 0
        fromTime = end[i]
        toTime = end[i] + 999
        for j in range(len(end)):
            if (end[j] >= fromTime and start[j] <= fromTime) or (start[j] >= fromTime and end[j] <= toTime) or (start[j] <= toTime and end[j] >= toTime) or (start[j] <= fromTime and end[j] >= toTime):
                count +=1
        answer = max(answer, count)
        
    return answer