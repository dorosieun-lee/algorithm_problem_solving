# SWEA 1961 숫자 배열 회전
import copy
T = int(input())

for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    new_arr = [[0]*N for _ in range(N)]
    transform = [[0]*3 for _ in range(N)]

    for col in range(3):
        #90도 회전
        for i in range(N):
            for j in range(N):
                new_arr[j][N-1-i] = arr[i][j]
        #print(new_arr)

        for row in range(N):
            transform[row][col] = ''.join(list(map(str,new_arr[row])))

        arr = copy.deepcopy(new_arr)

    print(f'#{test}')
    for i in range(N):
        print(*transform[i][:])