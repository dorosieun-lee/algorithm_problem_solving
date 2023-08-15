# SWEA 16523 미로찾기
# 10개 중 6개 맞음, 왜..?

T = int(input())

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for test in range(1, T+1):
    N = int(input())
    MAP = [input() for _ in range(N)]

    # 출발점 찾기 -> 2가 어디에 있는지
    for r in range(N):
        c = MAP[r].find('2')
        if c != -1:
            idx = [r, c]
            break

    visited = []
    stack = []

    visited.append(idx)
    stack.append(idx) # stack의 0번째 칸에는 출발점의 index가 담겨있다
    result = 0

    while True:
        if MAP[idx[0]][idx[1]] == '3':
            result = 1
            break
        for k in range(4): # 상하좌우를 탐색
            r = idx[0] + dr[k]
            c = idx[1] + dc[k]
            if (0 <= r < N) and (0 <= c < N) and [r, c] not in visited and MAP[r][c] != '1':
                # 경계를 벗어나지 않으며, 방문하지 않았던 곳이며, 갈 수 있는 길이면 idx = [r,c]로 바꾸고 반복문 종료(while으로 돌아감)
                idx = [r, c]
                if MAP[idx[0]][idx[1]] == '3': # 만약 그 곳이 도착점이면 길이 있음으로 result=1로 변경하고 반복문 종료
                    result = 1
                    break
                stack.append(idx) # 도착점은 아니고 그냥 길이면, stack에 추가 & 방문 표시
                visited.append(idx)
                break

        else:
            # 조건을 만족하는 셀이 상하좌우에 없으면 -> 왔던 길 되돌아감
            if stack: # stack이 비어있지 않으면,
                idx = stack.pop()
            else: # 더 갈길이 없고, 3을 만나지도 못했는데, stack이 비어버렸다 -> 갈 수 있는 경로가 없다
                break

    print(f'#{test} {result}')

