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

# zip 함수를 활용
T = int(input())


def rotation90(lst):
    result = []
    tmp =  list(zip(*lst))
    for line in tmp:
        result.append(line[::-1])

    return result


for test in range(1, T+1):
    N = int(input())
    MAP = [list(input().split()) for _ in range(N)] # NxN 행렬

    MAP90 = rotation90(MAP)
    MAP180 = rotation90(MAP90)
    MAP270 = rotation90(MAP180)

    print(f'#{test}')
    for i in range(N):
        print(''.join(MAP90[i]), ''.join(MAP180[i]), ''.join(MAP270[i]))