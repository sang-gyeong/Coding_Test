def solution(n):
    answer = 0
    a = [0] * (n+2)
    a[1] = 1
    a[2] = 2
    for i in range(3, n+1):
        a[i] = (a[i-1] + a[i-2]) % 1234567
    answer = a[n]
    return answer