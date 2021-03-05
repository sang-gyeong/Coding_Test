# 1시간 30분 소요
# 줄바꿈 문자 처리를 주의해야 함

import re


def solution(word, pages):
    answer = 0
    my_dict = {}
    result = []
    link_p = re.compile(r'<meta[^>]*content="https://([\S]*)"/>', re.M)
    out_p = re.compile(r'<a href="https://([\S]*)">', re.M)

    for page in pages:
        alpha_page = re.sub('[^a-zA-Z]+', ' ', page.lower())
        basic_score = alpha_page.split().count(word.lower())
        my_link = link_p.search(page)
        out_links = out_p.findall(page)
        my_dict[my_link.group(1)] = [basic_score, len(
            out_links), out_links, basic_score]

    for key in my_dict:
        [basic_score, out_link, links, link_score] = my_dict[key]
        for link in links:
            if link in my_dict and out_link != 0:
                my_dict[link][3] += basic_score/out_link

    for key in my_dict:
        result.append(my_dict[key][3])
    max_score = max(result)
    for i in range(len(result)):
        if result[i] == max_score:
            answer = i
            break

    return answer
