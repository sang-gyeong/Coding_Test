import re


def solution(s):
    answer = ''
    item = re.findall('[A-Z][a-z]|[A-Z]', s)
    num = [num for num in s if num.isdigit()]
    if len(item) != len(num):
        return 'error'

    n = len(item)
    for i in range(n):
        answer += item[i]
        answer = answer + num[i] if num[i] != '1' else answer

    return answer


def main():
    result = solution('HO21')
    print(result)
    result = solution('CO12')
    print(result)
    result = solution('HSO214')
    print(result)
    result = solution('NaCl1')
    print(result)
    result = solution('ClAZTi340')
    print(result)


main()
