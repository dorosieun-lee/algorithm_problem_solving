# SWEA 4861 회문
# 슬라이싱 안쓰고 해보기
T = int(input())

for test in range(1, T+1):
    N, M = list(map(int, input().split()))
    MAP = [list(input()) for _ in range(N)] # NxN 문자열
    is_row = False
    idx = [0, 0]

    for i in range(N): # 행 우선 탐색
        for j in range(N-M+1):
            for m in range(0, M//2):
                dj = j + m
                if MAP[i][dj] != MAP[i][M+j-m-1]:
                    break
            else:
                is_row = True
                idx = [i, j]
                break

    if not is_row:  # 행 탐색에서 못 찾았으면 열 탐색하기
        for i in range(N):
            for j in range(N-M+1):
                for m in range(0, M//2):
                    dj = j + m
                    if MAP[dj][i] != MAP[M+j-m-1][i]:
                        break
                else:
                    idx = [j, i]
                    break


    if is_row:
        # print('r', idx)
        word = ''
        for m in range(M):
            word += MAP[idx[0]][idx[1]+m]
    else:
        # print('c', idx)
        word = ''
        for m in range(M):
            word += MAP[idx[0]+m][idx[1]]
    print(f'#{test} {word}')


"""
강사님 코드 -> MAP 90도 뒤집어서 이어 붙이기
T = int(input())

for test in range(1, T+1):
    N, M = list(map(int, input().split()))
    MAP = [list(input()) for _ in range(N)]
    MAP += list(zip(*MAP))
    
    for m in MAP:
        for i in range(0, N - M + 1):
            if m[i:i+M] == m[i:i+M][::-1]:
                result = m[i:i+M]
                break
                
    result = ''.join(result)
    
    print(f'#{test} {result}')
"""