from itertools import combinations


def solution(answer_sheet, sheets):
    answer = 0
    n = len(sheets)
    m = len(answer_sheet)
    cases = combinations(range(n), 2)
    for case in cases:
        (s1, s2) = case
        total = 0
        max_len = 0
        flag = -1
        for i in range(m):
            if sheets[s1][i] == sheets[s2][i] and sheets[s2][i] != answer_sheet[i]:
                total += 1
                flag = 1 if flag == -1 else flag + 1
            else:
                max_len = flag if flag > max_len else max_len
                flag = -1
        max_len = flag if flag > max_len else max_len
        score = total + max_len**2
        answer = score if score > answer else answer

    return answer


def main():
    test1 = "4132315142"
    test2 = "53241"
    test3 = "24551"

    sheets1 = ["3241523133", "4121314445",
               "3243523133", "4433325251", "2412313253"]
    sheets2 = ["53241", "42133", "53241", "14354"]
    sheets3 = ["24553", "24553", "24553", "24553"]

    print('test1 : ', solution(test1, sheets1))
    print('test2 : ', solution(test2, sheets2))
    print('test3 : ', solution(test3, sheets3))


main()
