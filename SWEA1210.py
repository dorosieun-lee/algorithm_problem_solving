# SWEA 1210 Ladder1

T = 10 # test case: 10개

for test in range(1, T+1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    j = ladder[99].index(2)
    i = 99

    dir = [1, 0, 0] # 진행방향 인덱스 up, left, right -> 일단 위로 가는 걸로 시작

    while i > 0:
        if dir[0] == 1: # 올라가는 중이었다
            if j != 0 and ladder[i][j - 1] == 1: # 왼쪽 갈 수 있나?
                dir[1] = 1
                dir[0] = 0
                j -= 1
            elif j != 99 and ladder[i][j+1] == 1: # 오른쪽 갈 수 있나?
                dir[2] = 1
                dir[0] = 0
                j += 1
            else: # 안되면 그냥 가던 길 계속 가
                i -= 1

        if dir[1] == 1: # 왼쪽으로 가는 중이었다
            if ladder[i - 1][j] == 1: # 올라갈 수 있나?
                dir[0] = 1
                dir[1] = 0
                i -= 1
            else: # 안되면 그냥 가던 길 계속 가
                j -= 1

        if dir[2] == 1: # 오른쪽으로 가는 중이었다
            if ladder[i - 1][j] == 1: # 올라갈 수 있나?
                dir[0] = 1
                dir[2] = 0
                i -= 1
            else: # 안되면 그냥 가던 길 계속 가
                j += 1


    print(f'#{test} {j}')