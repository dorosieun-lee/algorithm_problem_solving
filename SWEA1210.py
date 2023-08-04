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

"""
강사님 코드
T = 10
for test in range(1, T+1):
    input() # test case 번호는 읽기만하고 저장 안함
    MAP = [list(map(int, input().split())) for _ range(100)]
    # 2차원 리스트 만들기 로직

    # 도착점부터 올라갈거다
    # 올라가는 길에 좌, 우를 우선할거다
    # 반복문 -> 내가 출발점에 도달할 때까지

    for n in range(100):
        if MAP[99][n] == 2:
            x = n
            break

    # print(x) # 도착점의 열 번호
    # 출발점
    y = 99

    while True: # 몇번 반복해야하는지 모르니까 while문 사용 -> while문은 종료조건이 중요
        if y == 0: # 첫번째 행에 도달하면 끝내겠다!
            break

        # MAP의 가장 오른쪽 경계를 벗어나지 않으면서 오른쪽에 1이 존재하는 경우
        if x < 99 and MAP[y][x+1] == 1:
            while x < 99 and MAP[y][x+1] == 1: # 갈 수 있을때까지 계속 오른쪽으로 가
                x += 1
            else:
                y -= 1 # 안돼? 그럼 위로 올라가

        # MAP의 가장 왼쪽 경계를 벗어나지 않으면서 왼쪽에 1이 존재하는 경우
        elif x > 0 and MAP[y][x-1] == 1:
            while x > 0 and MAP[y][x-1] == 1: # 갈 수 있을때까지 계속 왼쪽으로 가
                x -= 1
            else:
                y -= 1 # 안돼? 그럼 위로 올라가

        else:
            y -= 1
    print(f'#{test} {x}')
"""
