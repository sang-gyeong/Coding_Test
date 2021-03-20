# id, name, pid 준담에 리프트리에 해당하는 애들 doll이 word에 정확히 일치하는 순서대로 부모/자식 느낌으로 출력해서 리스트에 담아 반환


import re


class Item:
    def __init__(self, id, name, pid):
        self.id = id
        self.name = name
        self.pid = pid


def solution(data, word):
    n = len(data)
    answer = []
    error = f"Your search for ({word}) didn't return any results"

    pid_list = [False] * (n+1)
    leaf_dolls = []
    items = {}
    for doll in data:
        [id, name, pid] = doll.split()
        pid_list[int(pid)] = True
        items[int(id)] = [name, int(pid)]

    for i in range(n):
        if i != 0 and pid_list[i+1] == False:
            leaf_dolls.append(data[i].split())
    for i in range(len(leaf_dolls)):
        [id, name, pid] = leaf_dolls[i]
        find = re.findall(word, name)
        leaf_dolls[i].append(len(find))
        leaf_dolls[i].append(name.find(word))

    leaf_dolls.sort(key=lambda x: (-x[3], x[4]))
    for d in leaf_dolls:
        result = ""
        [id, name, pid, d, e] = d
        [name2, p] = items[int(pid)]
        if p != 0:
            [a, b] = items[int(p)]
            answer.append(a+"/"+name2+"/"+name)
        else:
            answer.append(name2+"/"+name)

    answer = [error]
    return answer
