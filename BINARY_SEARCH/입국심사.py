def solution(n, times):
    answer = 0
    start = 0
    end = max(times) * n
    times = sorted(times)
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for time in times:
            count += mid // time
            if count >= n:
                break
        if count >= n:
            answer = mid
            end = mid-1
        else:
            start = mid + 1

    return answer
