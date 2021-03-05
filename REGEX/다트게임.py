import re


def solution(dartResult):
    answer = 0
    scores = []
    BONUS = {'S': 1, 'D': 2, 'T': 3}
    results = re.findall('[0-9]+[SDT][#*]*', dartResult)
    for result in results:
        isAtcha = -1 if '#' in result else 1
        score = re.match('[0-9]+', result)
        bonus = re.search('[SDT]', result)
        scores.append(int(score.group())**BONUS[bonus.group()]*isAtcha)

    for i in reversed(range(len(results))):
        if "*" in results[i]:
            scores[i] *= 2
            if (i != 0):
                scores[i-1] *= 2

    answer = sum(scores)
    return answer
