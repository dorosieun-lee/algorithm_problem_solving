# SWEA 1979 어디에 단어가 들어갈 수 있을까
# 1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
# 2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)
# 순회하면서 열이든, 행이든 연속된 1의 갯수를 세서 K개인 곳이 몇개인지 카운트

T = int(input())

for test in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1: 흰색 부분
    # 0: 검은색 부분

    count = 0
    # 행 우선 순회
    for i in range(N):
        sub_cnt = 0
        for j in range(N):
            if arr[i][j] == 1: # 1 만나면 sub_cnt +1
                sub_cnt += 1
            if arr[i][j] == 0: # 0 만나면 sub_cnt 초기화
                sub_cnt = 0

            if j != N-1 and sub_cnt == K: # 끝 행이 아니고 sub_cnt가 단어 갯수만큼 있으면
                if arr[i][j+1] == 0: # 바로 다음 열이 0인지 확인하고 count + 1, sub_cnt는 초기화
                    count += 1
                    sub_cnt = 0
                    #print(f'{count}: row{i} {j}')
            if j == N-1 and sub_cnt == K: # 마지막 행에 도달하면 sub_cnt가 단어의 갯수와 같은지 확인
                count += 1
                sub_cnt = 0
                #print(f'{count}: row{i} {j}')

    """
    강사님 코드 (코드가 더 간결함)
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
        if arr[i][j] == 1:
            cnt += 1
        elif j = N-1 or arr[i][j] == 0:
            if cnt == K:
                ans += 1
            cnt = 0
        
    """

    # 열 우선 순회
    for j in range(N):
        sub_cnt = 0
        for i in range(N):
            if arr[i][j] == 1: # 1 만나면 sub_cnt +1
                sub_cnt += 1
            if arr[i][j] == 0: # 0 만나면 sub_cnt 초기화
                sub_cnt = 0

            if i != N - 1 and sub_cnt == K: #끝 열이 아니고 sub_cnt가 단어 갯수만큼 있으면
                if arr[i + 1][j] == 0: # 바로 다음 열이 0인지 확인하고 count + 1, sub_cnt는 초기화
                    count += 1
                    sub_cnt = 0
                    #print(f'{count}: col{j} {i}')
            if i == N - 1 and sub_cnt == K: # 마지막 열에 도달하면 sub_cnt가 단어의 갯수와 같은지 확인
                count += 1
                sub_cnt = 0
                #print(f'{count}: col{j} {i}')

    print(f'#{test} {count}')