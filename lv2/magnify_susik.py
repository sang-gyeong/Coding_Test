import re
import copy
from itertools import permutations

def solution(expression):
    answer = 0
    permutation = list(permutations(["+", "-", "*"]))
    nums = re.findall(r"[\d]+", expression)
    susiks = re.findall(r"[\D]+", expression)
    for pers in permutation :
        testNums = copy.deepcopy(nums)
        testSusiks = copy.deepcopy(susiks)
        for i in range(3):
            while pers[i] in testSusiks:
                index = testSusiks.index(pers[i])
                tmp = eval(testNums[index] + pers[i] + testNums[index+1])
                testNums[index] = str(tmp)
                testNums.pop(index+1)
                testSusiks.pop(index)
        result = abs(int(testNums[0]))
        if result > answer : answer = result
    
    return answer