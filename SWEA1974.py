# SWEA 1974 스도쿠 검증
T = int(input())

for test in range(1, T+1):
    sdoku = [list(map(int, input().split())) for _ in range(9)] # 9x9 array
    result = 1

    for i in range(9):
        if len(set(sdoku[i])) != 9:
            # print('a')
            result = 0
            break
        if len(set(list(zip(*sdoku))[i])) != 9:
            # print('b')
            result = 0
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = []
            for k in range(3):
                nums.extend(sdoku[i+k][j:j + 3])

            if len(set(nums)) != 9:
                # print('c')
                result = 0
                break

        if result == 0:
            break

    print(f'#{test} {result}')