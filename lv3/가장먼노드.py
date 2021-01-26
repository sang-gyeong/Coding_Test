import heapq
import sys


def dijkstra(start, distance, graph):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(n, edge):
    answer = 0
    INF = int(1e9)
    m = len(edge)
    
    start = 1
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)
    
    for [a, b] in edge:
        graph[a].append((b,1))
        graph[b].append((a,1))
                       
    dijkstra(start, distance, graph)
    
    max_dist = max(distance[1:])
    for i in range(1, n+1):
        if distance[i] == max_dist:
            answer += 1

    
    
    return answer