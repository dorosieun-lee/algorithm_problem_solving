# SWEA 2117 홈 방범 서비스

def calc_price(K):
    return K * K + (K - 1) * (K - 1)


def count_home(K, row, col):
    if K == 1:
        if city_MAP[row][col] == 1:
            return 1
        else:
            return 0

    else: # K가 2 이상이면
        home_cnt = 0
        dist = K-1
        j_dist = list(range(0, K-1)) + list(range(K-1, -1, -1))
        # 마름모 꼴로, 방범 지역 순회하면서
        for i in range(-dist, dist+1):
            for j in range(-j_dist[i+dist], j_dist[i+dist]+1):
                nrow = row - i
                ncol = col - j
                if (0 <= nrow < N) and (0 <= ncol < N): # 경계 안에 있으면서
                    if city_MAP[nrow][ncol] == 1:
                        home_cnt += 1
        return home_cnt


T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split()) # 도시의 크기, 하나의 집이 지불할 수 있는 비용
    city_MAP = [list(map(int, input().split())) for _ in range(N)]

    N_home_list = []
    K = 1 # 1에서부터 보자고~
    while True:
        for row in range(N):
            for col in range(N):
                N_home = count_home(K, row, col)
                benefit = M * N_home - calc_price(K)
                if benefit >= 0:
                    N_home_list.append(N_home)

        if ((K-1) // 2) * 2 + 1 > N:
            break

        K += 1

    print(f'#{test} {max(N_home_list)}')