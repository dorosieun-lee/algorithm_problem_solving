# 중계기
#
# 가로와 세로가 N x N 크기인 정사각형 모양의 어느 한 마을에서 중계기를 설치하려고 한다.
# 마을 주민 모두에게 원활한 통신 서비스를 제공하기 위해, 마을에 있는 모든 집들이
# 중계기의 통신 범위 안에 포함되도록 설치하되, 통신 범위를 최소화 하는 것이 목표이다.
# 중계기는 입력으로 주어진 위치 (y, x)에 설치된다.
# 중계기의 통신 범위는 원 모양으로, 반지름 R의 범위는 1 이상 정수이다.
# 마을에 있는 집의 위치와 중계기의 위치가 입력으로 주어졌을 때, 마을의 모든 집들을 포함할수 있는
# 중계기 통신범위의 반지름 R의 최소값을 구하는 프로그램을 작성하라.
#
# [제약사항]
# 1. 지도의 크기 N은 5이상 10 이하의 정수이다 (5 <= N <= 10)
# 2. 좌표는 좌측 상단부터 (0, 0)으로 시작한다. 지도의 크기는 N x N 크기의 정사각형이며, 모든 집들의 좌표는 격자점 위에 있으므로, 입력으로 주어지는 2차원 Map Data의 크기는 (N+1)^2이 됨을 유의하라.
# 3. 중계기의 통신 범위가 최대일 경우에도, 모든 집들이 포함되지 않는 경우는 입력으로 주어지지 않는다.
# 4. 중계기 통신범위에 포함되는지 여부는 아래와 같이 판단할 수 있다.
# 집과 중계기의 좌표가 각각 (hy, hx), (y, x)일 경우, 거리 D의 제곱은 다음과 같다.
# D^2 = (hy - y)^2 + (hx - x)^2
# 집과 중계기 간 거리 D의 제곱이 반지름 R의 제곱보다 작거나 같을 경우, 중계기의 통신 범위에 포함된다.

T = int(input())

for test in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N+1)] #(N+1) x (N+1) 이차원 배열
    houses = []
    for row in range(N+1):
        for col in range(N+1):
            if MAP[row][col] == 1:
                houses.append([row,col])
            if MAP[row][col] == 2:
                point = [row, col]

    result = 0
    for house in houses:
        dist = ((house[0] - point[0])**2 + (house[1] - point[1])**2)**(0.5)
        if dist != int(dist):
            dist = int(dist) + 1
        result = max(int(dist), result)

    print(f'#{test} {result}')

'''
강사님 코드
T = int(input())

for t in range(1,T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N + 1)]
    repeater = ()


    def findRepeater():

        for i in range(N + 1):
            for j in range(N + 1):
                if MAP[i][j] == 2:
                    return i, j


    def findDistant(i, j):
        sqrt = []

        for hi in range(N + 1):
            for hj in range(N + 1):
                if MAP[hi][hj] == 1:
                    sqrt.append((abs(hi - i) ** 2) + abs(hj - j) ** 2)

        return max(sqrt)


    repeater = findRepeater()
    value = findDistant(repeater[0], repeater[1])

    # 입력 n 이있을때, 최대거리는 (n-0)**2 + (n-0)**2이다.
    # 현재 문제에서는 최대 n이 10이였으므로, 100+100 -> 제곱해서 200이 되는수보단 작다
    # 15*15를 하면, 225로 유효범위를 넘을 수 있다
    for i in range(15):
        if i ** 2 >= value:
            print(f"#{t} {i}")
            break
'''