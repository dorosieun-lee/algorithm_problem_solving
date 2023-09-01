# 프로그래머스 더 맵게
# 알고리즘 로직보다는 heapq를 쓸 수 있는가가 포인트라고 생각함.
# heapq를 쓰면 속도가 매우 빨라짐! (정렬이 자동)

def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)
    mix_cnt = 0
    while scoville[0] < K and len(scoville) >= 2:
        first_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)
        heapq.heappush(scoville, first_min + second_min * 2)
        mix_cnt += 1

    if scoville[0] >= K:
        answer = mix_cnt
    else:
        answer = -1

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))