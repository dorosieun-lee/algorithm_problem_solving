# SWEA 16504 Gravity
T = int(input())

for test in range(1, T+1):
    N = int(input())
    box_list = list(map(int, input().split()))

    max_gap = N-1

    drop_possible = [max_gap] * box_list[0] # 가장 왼쪽에 쌓인 상자 높이만큼의 빈 리스트 생성

    for i in range(box_list[0]):
        for j in range(1, N):
            if box_list[j] != 0:
                drop_possible[i] -= 1
                box_list[j] -= 1

    try:
        print(f'#{test} {max(drop_possible)}')
    except ValueError:
        print(f'#{test} 0')