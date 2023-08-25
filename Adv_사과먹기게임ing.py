# Adv 사과 먹기 게임

def find_apple(number):
    for row in range(N):
        for col in range(N):
            if MAP[row][col] == number:
                return (row, col)
    else:
        return False


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for test in range(1, 2):#T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]  # NxN 이차원 배열

    key = 2
    # 1: 상, 2: 우, 3: 하, 4: 좌 -> 초기 설정은 오른쪽 방향
    # key += 1: 우회전, key -= 1: 좌회전
    # 회전 후, if key <= 0: key = Key+4
    turn_cnt = 0
    number = 1
    point = [0, 0]
    while True:
        # print(number, turn_cnt)
        apple = find_apple(number)
        if not apple:
            break

        if key in [2, 4]:  # 우측이나 좌측으로 방향이 설정되어 있으면
            if key == 2 and apple[1] < point[1]: # 우측으로 방향 설정이 되어 있는데, 사과는 좌측에 있다면
                # 상하 중 어디에 있는지 확인하고 키 바꾸고 continue
                if apple[0] > point[0]: # 위에 있다
                    key -= 1
                    turn_cnt += 3
                else:
                    key += 1
                    turn_cnt += 1

            if key == 4 and apple[1] > point[1]: # 좌측으로 방향 설정이 되어 있는데, 사과는 우측에 있다면
                # 상하 중 어디에 있는지 확인하고 키 바꾸고 continue
                if apple[0] < point[0]: # 아래에 있다
                    key -= 1
                    turn_cnt += 3
                else:
                    key += 1-4
                    turn_cnt += 1

            while True:
                if point[1] == apple[1]:  # 사과가 있는 열까지 이동
                    break
                point[0] += di[key - 1]
                point[1] += dj[key - 1]
            if MAP[point[0]][point[1]] == number:  # 사과 만났으면, 사과 숫자 올리고 다음으로 넘어감
                number += 1
                continue

            if apple[0] < point[0]:  # 사과가 플레이어 위에 있으면,
                if key == 2:  # 오른쪽으로 이동 중이었으면, 좌회전 (좌회전 못함 -> 대신 우회전 세번하면 좌회전과 같음)
                    key -= 1
                    turn_cnt += 3
                else:  # 왼쪽으로 이동 중이었으면, 우회전
                    key += 1 - 4  # 4+1해서 5가 되었으므로 1로 바꿔줌
                    turn_cnt += 1
            else:  # 사과가 플레이어 아래에 있으면,
                if key == 2:  # 오른쪽으로 이동 중이었으면, 우회전
                    key += 1
                    turn_cnt += 1
                else:  # 왼쪽으로 이동 중이었으면, 좌회전 (좌회전 못함 -> 대신 우회전 세번하면 좌회전과 같음)
                    key -= 1
                    turn_cnt += 3

        if key in [1, 3]:  # 위나 아래로 방향이 설정되어 있으면
########### 여기 상하에 맞게 바꿔야함!!!!!!!!!!!!!!!!!!!
            if key == 2 and apple[1] < point[1]:  # 우측으로 방향 설정이 되어 있는데, 사과는 좌측에 있다면
                # 상하 중 어디에 있는지 확인하고 키 바꾸고 continue
                if apple[0] > point[0]:  # 위에 있다
                    key -= 1
                    turn_cnt += 3
                else:
                    key += 1
                    turn_cnt += 1

            if key == 4 and apple[1] > point[1]:  # 좌측으로 방향 설정이 되어 있는데, 사과는 우측에 있다면
                # 상하 중 어디에 있는지 확인하고 키 바꾸고 continue
                if apple[0] < point[0]:  # 아래에 있다
                    key -= 1
                    turn_cnt += 3
                else:
                    key += 1 - 4
                    turn_cnt += 1

            while True:
                if point[0] == apple[0]:  # 사과가 있는 열까지 이동
                    break
                point[0] += di[key - 1]
                point[1] += dj[key - 1]
            if MAP[point[0]][point[1]] == number:  # 사과 만났으면, 사과 숫자 올리고 다음으로 넘어감
                number += 1
                continue

            if apple[1] > point[1]:  # 사과가 플레이어 오른쪽에 있으면,
                if key == 1:  # 위쪽으로 이동 중이었으면, 우회전
                    key += 1
                    turn_cnt += 1
                else:  # 아래쪽(3)으로 이동 중이었으면, 좌회전 (좌회전 못함 -> 대신 우회전 세번하면 좌회전과 같음)
                    key -= 1
                    turn_cnt += 3
            else:  # 사과가 플레이어 왼쪽에 있으면
                if key == 1:  # 위쪽으로 이동 중이었으면, 좌회전 (좌회전 못함 -> 대신 우회전 세번하면 좌회전과 같음)
                    key -= 1 + 4  # 1-1 = 0 이 되니까 4로 바꿔줌
                    turn_cnt += 3
                else:  # 아래쪽으로 이동 중이었으면, 우회전
                    key += 1
                    turn_cnt += 1

    print(f'#{test} {turn_cnt}')

