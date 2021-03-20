def solution(table, languages, preference):
    answer = ''
    my_dict = {}
    result = {}
    for item in table:
        [job, l1, l2, l3, l4, l5] = item.split()
        my_dict[job] = [0, l5, l4, l3, l2, l1]

    for i in range(len(languages)):
        prefer = preference[i]
        for job in my_dict:
            if languages[i] in my_dict[job]:
                score = my_dict[job].index(languages[i])
                if result.get(job) == None:
                    result[job] = int(score * prefer)
                else:
                    result[job] += int(score * prefer)
    sorted_result = sorted(result.items(), key=lambda x: (-x[1], x[0]))
    answer = sorted_result[0][0]
    return answer
