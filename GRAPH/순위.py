def solution(n, results):
    answer = 0
    win, lose = {}, {}
    for i in range(1, n+1):
        win[i] = set()
        lose[i] = set()

    for [w, l] in results:
        win[w].add(l)
        lose[l].add(w)

    for i in range(1, n+1):
        for winner in lose[i]:
            win[winner].update(win[i])
        for loser in win[i]:
            lose[loser].update(lose[i])

    for i in range(1, n+1):
        count = len(win[i]) + len(lose[i])
        if count == n-1:
            answer += 1

    return answer
