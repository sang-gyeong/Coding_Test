import re


def solution(inp_str):
    answer = []
    item = '~!@#$%^&*'
    my_set = set(inp_str)
    if len(inp_str) < 8 or len(inp_str) > 15:
        answer.append(1)
    result = re.findall('[^A-Za-z0-9~!@#$%^&*]', inp_str)
    if len(result) > 0:
        answer.append(2)
    count = 0
    check = [False] * 4
    for s in inp_str:
        if s.isupper() and check[0] == False:
            count += 1
            check[0] = True
        elif s.islower() and check[1] == False:
            count += 1
            check[1] = True
        elif s.isdigit() and check[2] == False:
            count += 1
            check[2] = True
        elif s in item and check[3] == False:
            count += 1
            check[3] = True
    if count < 3:
        answer.append(3)

    count = 1
    tmp = inp_str[0]
    for s in inp_str[1:]:
        if s == tmp:
            count += 1
        else:
            tmp = s
            count = 1
        if count >= 4:
            answer.append(4)
            break

    for s in my_set:
        tmp = inp_str.count(s)
        if tmp >= 5:
            answer.append(5)

    if len(answer) == 0:
        answer.append(0)

    return answer
