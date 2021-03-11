def solution(numbers, target):
    result = go(numbers, 0, target, 0)
    answer = result
    return answer


def go(numbers, index, target, S):
    if index == len(numbers):
        if S == target:
            return 1
        return 0
    value = numbers[index]
    return go(numbers, index+1, target, S+value)
    + go(numbers, index+1, target, S-value)
