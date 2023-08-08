# 사각형 그리기 게임

# 사각형 그리기 게임에는 N x N 크기의 게임판이 주어진다.
# 이 게임의 목표는 최대한 면적이 큰 사각형을 몇 개 그릴 수 있는가?를 구하는 것이다.
# 사각형을 그리는 데에는 아래 두가지 조건을 충족해야만 한다.
# [1] 특정 좌표를 기준으로, "우측 하단"의 방향으로 사각형을 그릴 수 있다.
# [2] 왼쪽 상단 좌표의 값과 우측 하단 좌표의 값이 동일해야 한다.
# N x N 크기의 게임판이 주어졌을 때, 최대 면적의 사각형을 규칙대로 그릴 수 있는 총 사각형의 개수를 구하라.

# 시간 초과 -> 반복 횟수를 줄일 수 없을까? -> MAX로 반복문 도는 횟수에 제한을 둠으로써 시간을 줄일 수 있었음.

T = int(input())

for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt_list = [0] * 21 # 게임 판의 값: 1 ~ 20 -> 인덱스로 쓸거라서 21칸

    for i in range(N):
        for j in range(N):
            cnt_list[arr[i][j]] += 1

    area = []
    MAX = 0
    for i in range(N):
        for j in range(N):
            # arr 내에 arr[i][j]에 해당하는 수가 있으면 아래 과정을 진행, 없으면 area에 1 저장하고 다음 요소로 이동하고 싶음
            # 위에서 cnt_list를 만들어서 배열 내에 arr[i][j]가 몇번 나오지는지 미리 세어 놓음 -> 반복문 도는 횟수 단축
            if cnt_list[arr[i][j]] >= 2 and (N-i+1)*(N-j+1) >= MAX:
                for di in range(0, N-i):
                    for dj in range(0, N-j):
                        if arr[i][j] == arr[i+di][j+dj]:
                            area.append((di+1) * (dj+1))
                            MAX = max(MAX, (di+1) * (dj+1))
            else:
                area.append(1)

    cnt = area.count(max(area))

    print(f'#{test} {cnt}')