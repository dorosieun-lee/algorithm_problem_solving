# SWEA 4408 자기 방으로 돌아가기

T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    hr = 1
    for i in range(N):
        is_overlap = False
        arr = [0] * 401
        arr[lst[i][0]:lst[i][1]+1] = [1] * (lst[i][1] - lst[i][0] + 1)
        for j in range(i+1, N):
            if is_overlap:
                break
            for k in range(lst[j][0], lst[j][1]+1):
                if arr[k] == 1: # 겹치는 구간이 있으면
                    hr += 1
                    is_overlap = True
                    break

    print(f'#{test} {hr}')