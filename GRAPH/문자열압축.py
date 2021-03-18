def solution(s):
    n = len(s)
    answer = n
    for length in range(1, (n//2) + 1):
        result = ""
        tmp = s[:length]
        count = 1
        for i in range(length, n, length):
            obj = s[i:i+length]
            if tmp == obj:
                count += 1
            else:
                if count == 1:
                    result += tmp
                else:
                    result += str(count) + tmp
                count = 1
                tmp = obj
        if count == 1:
            result += tmp
        else:
            result += str(count) + tmp
        answer = len(result) if answer > len(result) else answer

    return answer
