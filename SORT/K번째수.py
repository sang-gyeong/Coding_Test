def solution(array, commands):
    answer = []

    for c in commands:
        newArray = sorted(array[c[0] - 1: c[1]])
        answer.append(newArray[c[2] - 1])

    return answer
