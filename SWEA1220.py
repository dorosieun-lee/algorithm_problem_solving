# SWEA 1220 Magnetic

# 파란색은 N극에 끌림, 빨간색은 S극에 끌림
# N극은 위쪽, S극은 아래쪽에 위치
# 1: 아래로 감(S극에 끌림), 2: 위로 감(N극에 끌림)
# 교착상태의 개수를 반환
# 한쪽 방향으로 움직이는 자성체의 개수가 많더라도 반대 방향으로 움직이는 자성체가 하나라도 있으면 교착 상태가 됨

for test in range(1, 11):
    N = int(input())
    Magnetic = [list(map(int, input().split())) for _ in range(N)] # 100x100 2차원 배열

    cnt = 0
    for col in range(N):
        flag = 'blue'
        for row in range(N):
            if Magnetic[row][col] == 1: # 1 위에서 찾음
                flag = 'red'
            if flag == 'red' and Magnetic[row][col] == 2: # 1 위에 있고 그 다음에 2 찾음
                cnt += 1
                flag = 'blue'

    print(f'#{test} {cnt}')
