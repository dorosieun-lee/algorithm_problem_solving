# SWEA 4408 자기 방으로 돌아가기

T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ range(N)]

    for i in range(N):
        arr = [0] * 401
        arr[lst[i][0]:lst[i][1]+1] = [1] * (lst[i][1] - lst[i][0] + 1)
        for j in range(i, N):
            arr[lst[j][0]:lst[j][1]+1] = [1] * (lst[j][1] - lst[j][0] + 1)
            if arr.find(2) # list에서 find 안됨. 다른 메서드 찾아보기
