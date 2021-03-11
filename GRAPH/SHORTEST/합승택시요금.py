# 50분
# 플로이드 워셜 알고리즘

def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    graph = [[INF] * (n) for _ in range(n)]

    a -= 1
    b -= 1
    s -= 1

    for i in range(n):
        graph[i][i] = 0

    for fare in fares:
        [d, e, f] = fare
        d -= 1
        e -= 1
        graph[d][e] = f
        graph[e][d] = f

    for k in range(n):
        for d in range(n):
            for e in range(n):
                if graph[d][k] + graph[k][e] < graph[d][e]:
                    graph[d][e] = graph[d][k] + graph[k][e]

    for i in range(n):
        cost = graph[s][i] + graph[i][a] + graph[i][b]
        answer = min(answer, cost)

    return answer
