def solution(participant, completion):
    answer = ''
    my_dict = {}
    for p in participant:
        if my_dict.get(p) == None:
            my_dict[p] = 1
        else:
            my_dict[p] += 1
    for c in completion:
        my_dict[c] -= 1
        if my_dict[c] == 0:
            del my_dict[c]
    for key in my_dict:
        answer = key
    return answer
