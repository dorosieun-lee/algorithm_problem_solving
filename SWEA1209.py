# SWEA 1209 Sum
T = 10 # 테스트 케이스 갯수
# 각 행의 합, 열의 합, 대각선의 합 중 최댓값을 구해라
for _ in range(1, T+1):
    test = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)] # 100X100 행렬
    sum_list = []

    r_axis_sum = 0 # 0,0에서 오른쪽 아래로 내려가는 대각선 합
    l_axis_sum = 0 # 0, 99에서 왼쪽 아래로 내려가는 대각선 합
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j] # 행 고정, 열 순회
            col_sum += arr[j][i] # 열 고정, 행 순회
            if i == j:
                r_axis_sum += arr[i][j]
            if i + j == 100 - 1:
                l_axis_sum += arr[i][j]
        sum_list.extend([row_sum, col_sum])

    sum_list.extend([r_axis_sum, l_axis_sum])

    print(f'#{test} {max(sum_list)}')