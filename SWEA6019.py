# SWEA 6019 기차 사이의 파리

T = int(input())

for test in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # 파리의 속력 * 왔다 갔다 할 수 있는 횟수
    # 왔다 갔다 할 수 있는 횟수 = 처음 기차 사이의 거리 / (A기차의 속력 + B기차의 속력)
    distance = format(F * (D / (A + B)), '0.6f') # 오차범위가 10**(-6) 이므로
    print(f'#{test} {distance}')