# SWEA 9367 점점 커지는 당근의 개수
# 좀 더 간결하고 빠르게 풀 수 있을 것 같은데..!!

T = int(input())

for test in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))

    cnt = 0
    cnt_list = []
    for i in range(1, N):
        if (carrot[i] - carrot[i-1]) > 0 :
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 0

    cnt_list.append(cnt)

    result = 0 if max(cnt_list) == 1 else max(cnt_list)+1

    print(f'#{test} {result}')

