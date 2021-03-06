def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        _tree = [s for s in skill_tree if s in skill]
        skill_list = list(skill)
        flag = True
        for t in _tree:
            if skill_list[0] == t:
                skill_list = skill_list[1:]
            else:
                flag = False
        answer = answer+1 if flag == True else answer

    return answer
