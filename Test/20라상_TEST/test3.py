def solution(s, n):
    results = []
    answer = 0
    go(s, 0, n, 0, results)
    answer = max(results)
    return answer


def go(s, index, n, max_len, results):
    if index == len(s):
        results.append(max_len)
        return
    if s[index] == '1':
        go(s, index+1, n, max_len+1, results)
    else:
        results.append(max_len)
        if n > 0:
            go(s, index+1, n-1, max_len+1, results)
        go(s, index+1, n, 0, results)


def main():
    test1 = "111011110011111011111100011111"
    test2 = "001100"
    n1 = 3
    n2 = 5

    print('test1 : ', solution(test1, n1))
    print('test2 : ', solution(test2, n2))


main()
