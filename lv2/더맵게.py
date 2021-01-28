import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for food in scoville :
        heapq.heappush(heap, food)
    while(heap[0] < K):
        try :
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            heapq.heappush(heap, first+(second*2))
            answer += 1
        except :
            return -1
    
    
    return answer