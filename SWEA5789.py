# SWEA 5789 현주의 상자 바꾸기
T = int(input())

for test in range(1, T+1):
    N, Q = map(int, input().split())
    lr_list = [list(map(int, input().split())) for _ in range(Q)]

    box = [0] * N

    for i in range(Q):
        for idx in range(lr_list[i][0], lr_list[i][1]+1):
            box[idx-1] = i+1

    print(f'#{test}', *box)