# 차르봄바

# 바이러스가 한 마을을 집어삼켰다
# 여기에 차르봄바라는 백신 폭탄을 떨어뜨려, 최대한 많은 바이러스를 제거하려고 한다.
# 차르봄바는 P 크기만큼으로 가로, 세로 방향으로 퍼져나가면서 해당 영역의 바이러스를 제거할 수 있다.
# N x N 크기의 마을의 한 위치에 차르봄바를 떨어뜨려, 가장 많은 바이러스를 제거했을 때 제거된 바이러스의 수를 구하여라

T = int(input())

for test in range(1, T+1):
    N, P = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    MAX = 0

    # 오른쪽, 아래, 왼쪽, 위 (델타 탐색)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            total = arr[i][j]
            for k in range(4):
                for l in range(1, P+1):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]

            MAX = max(total, MAX)


    print(f'#{test} {MAX}')