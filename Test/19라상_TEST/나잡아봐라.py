def solution(C, B):
    answer = 0
    go(C, B, 0, 1)
    return answer


def go(C, B, sec, move_gap):
    if C > 30 or B < 0 or B > 30:
        return -1

    if C == B:
        print(sec)
        quit()

    if B <= 15:
        go(C + move_gap, B*2, sec+1, move_gap+1)
    if B <= 29:
        go(C + move_gap, B+1, sec+1, move_gap+1)
    if B >= 1:
        go(C + move_gap, B-1, sec+1, move_gap+1)
    print(sec, C, B, move_gap)


def main():
    result = solution(11, 2)
    print(result)


main()
