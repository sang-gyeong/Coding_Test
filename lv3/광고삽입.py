def solution(play_time, adv_time, logs):
    answer = ''
    n = len(logs)
    play_time = timeToSec(play_time)
    adv_time = timeToSec(adv_time)
    
    
    start_times = [0]
    end_times = [adv_time]
    logs.sort()
    
    for log in logs:
        [start, end] = log.split('-')
        start_times.append(timeToSec(start))
        end_times.append(timeToSec(end))
    
    max_sec = 0
    for i in range(n) :
        totalSec = 0
        start = start_times[i]
        end = start + adv_time
        if end > play_time : 
            continue
        for j in range(n) :
            totalSec += getWatchSec(start, end, start_times[j], end_times[j])
        if totalSec > max_sec:
            max_sec = totalSec
            answer = secToTime(start)
            
    return answer

def getWatchSec(start, end, target_start, target_end) :
    if target_end < start or target_start > end:
        return 0
    elif target_start <= start and target_end >= start and target_end <= end:
        return target_end - start
    elif target_end >= end and target_start >= start and target_start <= end:
        return end - target_start
    elif target_start <= start and target_end >= end:
        return end - start
    elif target_start >= start and target_end <= end:
        return target_end - target_start
    
def addZero(num):
    if num < 10 :
        return "0" + str(num)
    else : return str(num)
    
def secToTime(sec):
    hour = sec // 3600
    min = (sec % 3600) // 60
    second = sec - (hour * 3600) - (min * 60)
    return addZero(hour) + ":" + addZero(min) + ":" + addZero(second)

def timeToSec(time):
    [hour, min, sec] = time.split(':')
    return int(hour) * 3600 + int(min) * 60 + int(sec)