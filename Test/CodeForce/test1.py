t = int(input())

for _ in range(t):
    answer = 0
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n-1):
        a, b = arr[i], arr[i+1]
        min_num = min(a, b)
        max_num = max(a, b)
        tmp = min_num
        while (max(max_num, tmp) / min(max_num, tmp)) > 2:
            tmp = tmp*2
            answer += 1
    print(answer)
