import re


def solution(s):
    answer = 0
    item = [('(', ')'), ('{', '}'), ('[', ']'), ('<', '>')]
    count = [0, 0, 0, 0]
    _s = ''.join(re.findall('[(|)|\{|\}|\[|\]|\<|\>]', s))
    for e in _s:
        for i in range(4):
            if e == item[i][0]:
                count[i] += 1
                break
            elif e == item[i][1]:
                count[i] -= 1
                if count[i] < 0:
                    return -1
                answer += 1
                break
    if sum(count) > 0:
        return -1
    return answer


def main():
    test1 = "Hello, world!"
    test2 = "line [plus]"
    test3 = "If (Count of eggs is 4,) {Buy milk.}"
    test4 = ">_<"
    test5 = "(()){[()}]"

    print('test1 : ', solution(test1))
    print('test2 : ', solution(test2))
    print('test3 : ', solution(test3))
    print('test4 : ', solution(test4))
    print('test5 : ', solution(test5))


main()
