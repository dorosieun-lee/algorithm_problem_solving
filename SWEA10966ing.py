# SWEA 10966 물놀이를 가자
# 땅에서 물로 가기 위한 최소 이동 거리
# 4개 돌고 제한시간 초과
# 어째서...!!!

from collections import deque

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def find_land(waters):  # BFS 방식
    visited = 0
    queue_list = [deque() for _ in range(len(waters))] # 물 블럭 개수만큼 큐 생성
    # print(queue_list)
    for i, w in enumerate(waters): # 각 큐의 첫번째 인덱스로 물의 인덱스를 추가
        queue_list[i].append(w)
    # dist[start[0]][start[1]] = 0

    while any(queue_list): # 큐 리스트 내에 어떤 큐라도 비어있지 않으면
        print(queue_list)
        if visited == N*M - len(waters): # 방문한 블럭 수가 (전체 블럭 수 - 물 블럭 수) 이면 땅 다 돌았다는 의미이므로, break
            break
        for i in range(len(waters)):
            try:
                row, col = queue_list[i].popleft()
                #print(f'{i}:', row, col)
            except:
                continue

            for k in range(4):
                nr, nc = row + move[k][0], col + move[k][1]
                if (0 <= nr < N) and (0 <= nc < M) and dist[nr][nc] == False and MAP[nr][nc] == 'L':
                    visited += 1
                    queue_list[i].append((nr, nc))
                    dist[nr][nc] = dist[row][col] + 1


T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(input()) for _ in range(N)]
    dist = [[False] * M for _ in range(N)]

    waters = []
    for row in range(N):
        for col in range(M):
            if MAP[row][col] == 'W':
                waters.append((row, col))

    find_land(waters)

    # print(dist)
    total = 0
    for line in dist:
        total += sum(line)

    print(f'#{test} {total}')