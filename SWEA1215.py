# SWEA 1215 회문1

T = 10

for test in range(1, T + 1):
    N = int(input())
    str_arr = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8 - N + 1):
            # 행 탐색
            word_r = []
            for k in range(N):
                word_r.append(str_arr[i][j + k])
            if word_r[0:N // 2] == word_r[N // 2 + 1 * (N % 2):][::-1]:
                # print('r',i,j, word_r)
                cnt += 1

            # 열 탐색
            word_c = []
            for k in range(N):
                word_c.append(str_arr[j + k][i])
            if word_c[0:N // 2] == word_c[N // 2 + 1 * (N % 2):][::-1]:
                # print('c',j, i, word_c)
                cnt += 1

    print(f'#{test} {cnt}')