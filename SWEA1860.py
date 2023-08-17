# SWEA 1860 진기의 최고급 붕어빵

T = int(input())

for test in range(1, T+1):
    N, M, K = map(int, input().split())
    times = list(map(int, input().split()))
    times.sort() # 오름차순 정렬
    sell = 0 # 팔린 붕어빵 누적
    flag = 'Possible'

    boonguh = 0
    for time in times:
        sell += 1 # 사람이 한 명 올 때마다 붕어빵 하나씩 팔림
        # 손님이 오는 시간에 만들어져있는 붕어빵의 개수 - 지금까지 팔린 붕어빵 개수
        boonguh = time // M * K - sell

        if boonguh < 0:
            flag = 'Impossible'
            break

    print(f'#{test} {flag}')
