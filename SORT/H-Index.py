def solution(citations):
    answer = 0
    citations.sort()
    for i in range(citations[len(citations) - 1]):
        l_cnt = 0
        m_cnt = 0
        for c in citations:
            if c >= i:
                m_cnt += 1
        l_cnt = len(citations) - m_cnt
        if m_cnt >= i and l_cnt <= i:
            answer = max(answer, i)

    return answer
