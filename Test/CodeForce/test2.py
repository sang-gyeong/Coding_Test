t = int(input())

for _ in range(t):
    answer = 0
    n = int(input())
    arr = list(map(int, input().split()))
    average = int(n / 3)
    count = [0, 0, 0]

    for num in arr:
        a = num % 3
        count[a] += 1

    max_ = max(count)
    max_index = 0
    for i in range(len(count)-1, -1, -1):
        if count[i] == max_:
            max_index = i
            print('max ', max_index)
            break

    gap = 0
    for k in range(max_index, max_index + 2):
        k = k % 3
        count[k] += gap
        gap = abs(count[k] - average)
        answer += gap
    print('answer', answer)
