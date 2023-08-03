# SWEA 1209 Sum
T = 10 # 테스트 케이스 갯수
# 각 행의 합, 열의 합, 대각선의 합 중 최댓값을 구해라
for _ in range(1, T+1):
    test = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)] # 100X100 행렬
    sum_list = []

    r_diag_sum = 0 # 0,0에서 오른쪽 아래로 내려가는 대각선 합
    l_diag_sum = 0 # 0,99에서 왼쪽 아래로 내려가는 대각선 합
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j] # 행 고정, 열 순회
            col_sum += arr[j][i] # 열 고정, 행 순회
            if i == j:
                r_diag_sum += arr[i][j]
            if i + j == 100 - 1:
                l_diag_sum += arr[i][j]
        sum_list.extend([row_sum, col_sum])

    sum_list.extend([r_diag_sum, l_diag_sum])

    print(f'#{test} {max(sum_list)}')

# 강사님 코드(엄청 짧음..!)
for t in range(1, 11):
    input()

    arr = [list(map(int, input().split())) for _ in range(100)]  # 100X100 행렬

    row_sum, col_sum, sum_diag1, sum_diag2 = 0, 0, 0, 0
    for i in range(100):
        # sum(arr[i]) => 행의 합
        # sum(zip(*arr)[i]) => 열의 합
        sum_diag1 += arr[i][i]
        sum_diag2 += arr[i][99-i]

    max_sum = max(sum(arr[i]), sum(zip(*arr)[i]) sum_diag1, sum_diag2)
    print(f'#{t} {max_sum}')

# 추가 설명
# lst = [[1,2,3],[1,2,3],[1,2,3]]
# print(*lst) -> 한꺼풀 벗겨진다 [[1,2,3],[1,2,3],[1,2,3]]
# -> [1,2,3] [1,2,3] [1,2,3]
#
#
# 리스트가 두개가 있다고 가정하자 짝궁을 맞춰줌 (길이가 맞아야함)
# lst1 = [1,2,3]
# lst2 = ['가','나','다']
#
# lst3 = zip(lst1,lst2)
# print(lst3)
# print(list(lst3))
#
# 우리문제에 적용하면
# print(list(zip(*lst))) 세로튜플을 구할 수 있다
#
# 애가 리스트니까 인덱싱
# print(list(zip(*lst))[0])
#
# 합 구하기
# print(sum(list(zip(*lst))[0]))