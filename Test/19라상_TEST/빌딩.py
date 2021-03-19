def solution(N, h):
    answer = 0
    start = 0
    target = 0
    while start < N and N-1-target > answer:
        for j in range(start+1, N):
            if h[start] <= h[j]:
                print(start, j)
                gap = j-start
                answer = gap if gap > answer else answer
                start = j
                break
        start += 1
    h.reverse()
    start = 0
    target = 0
    while start < N and N-1-start > answer:
        for j in range(start+1, N):
            if h[start] <= h[j]:
                print(start, j)
                gap = j-start
                answer = gap if gap > answer else answer
                start = j
                break
        start += 1
    return answer


def main():
    result = solution(10, [8, 4, 13, 8, 10, 2, 9, 7, 8, 12])
    print(result)


main()
