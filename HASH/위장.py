# <문제 풀이 핵심 아이디어>
# 하의 2개, 상의 3개의 경우,
# (하의 2개+안입은 경우) * (상의 3개 + 안입은 경우) = 3 * 4 = 12
# 그리고 전체에서 -1 (전부다 안입는 경우의 수를 뺀다)
# 즉 12 - 1 = 11

# combinations 라이브러리를 사용하지 않고 획기적으로 시간을 줄일 수 있는 방법이어서
# 다른 문제에서도 유용하게 사용해야겠다

def solution(clothes):
    answer = 0
    my_dict = {}
    my_clothes = []
    for [cloth, loc] in clothes:
        if my_dict.get(loc) == None:
            my_dict[loc] = 1
        else:
            my_dict[loc] += 1

    my_clothes = [value for value in my_dict.values()]
    n = len(my_clothes)

    tmp = 1
    for value in my_clothes:
        tmp *= value + 1
    answer = tmp - 1

    return answer
