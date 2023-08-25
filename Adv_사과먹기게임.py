# Adv 사과 먹기 게임

def find_apple(number): # number에 해당하는 사과의 위치를 찾는 함수
    for row in range(N):
        for col in range(N):
            if MAP[row][col] == number:
                return (row, col)
    else:
        return False

def transform_MAP(key):
    global MAP
    while key != 2:
        MAP = list(zip(*MAP[::-1])) # 시계방향 90도 회전
        key += 1
        if key > 4:
            key -= 4


T = int(input())
for test in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]  # NxN 이차원 배열

    # 우회전만으로 갈 수 있는 영역인지 확인하고(본인 좌표와 방향으로 판단 가능)
    # 영역별로 우회전 필요 횟수를 나눌 수 있음
    # 1: 상, 2: 우, 3: 하, 4: 좌 -> 초기 설정은 오른쪽 방향

    # 초기 설정
    point = [0, 0]
    key = 2
    number = 1
    turn_cnt = 0

    while True:
        #print(key, turn_cnt)
        transform_MAP(key) # key가 2가 되도록(우회적 방향이 되도록 MAP을 회전시킴)
        #print(MAP)

        point = find_apple(number-1)
        apple = find_apple(number)
        if not apple: # 더 이상 사과가 없으면 반복문 끝내기
            break

        # 우회전 1번으로 갈 수 있는 영역
        if (point[0] < apple[0]) and (apple[0] < N) and (point[1] < apple[1]) and (apple[1] < N):
            turn_cnt += 1
            number += 1
            key = 3

        # 우회전 2번으로 갈 수 있는 영역
        elif (point[0] < apple[0]) and (apple[0] < N) and (0 <= apple[1]) and (apple[1] < point[1]):
            turn_cnt += 2
            number += 1
            key = 4

        # 우회전 3번으로 갈 수 있는 영역
        elif (0 <= apple[0]) and (apple[0] < point[0]) and (0 <= apple[1]) and (apple[1] < point[1]):
            turn_cnt += 3
            number += 1
            key = 1

        # 우회전 4번으로 갈 수 있는 영역
        elif (0 < apple[0]) and (apple[0] < point[0]) and (point[1] < apple[1]) and (apple[1] < N):
            turn_cnt += 3
            number += 1
            key = 1

    print(f'#{test} {turn_cnt}')
