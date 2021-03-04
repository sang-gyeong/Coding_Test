import itertools

def solution(numbers):
    answer = 0
    n = [i for i in range(len(numbers))]
    numArr = [num for num in numbers]
    length = len(numbers)
    mySet = set()
    cases = []
    
    for i in range(1, length+1):
        permutation = itertools.permutations(n, i)
        for per in permutation:
            cases.append(per)
    
    for case in cases:
        now = ""
        for c in case:
            now += numbers[c]
        mySet.add(int(now))
    for num in mySet:
        if is_prime(num) == True:
            answer += 1
    
    return answer

def is_prime(num):
    if num == 1 or num == 0:
        return False
    else:
        n = int(num ** 0.5)

        for i in range(2, n + 1):
            if num % i == 0:
                return False
        return True