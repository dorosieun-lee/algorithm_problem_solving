# 삼성시 버스노선
T = int(input())

for test in range(1, T+1):
    N = int(input())
    ab_list = []
    for n in range(N):
        ab_list.append(list(map(int, input().split())))
    P = int(input())
    C_list = []
    for p in range(P):
        C_list.append(int(input()))

    """
    입력이 잘 되었는지 확인
    print(N)
    print(ab_list)
    print(P)
    print(C_list)
    """

    cnt_busline = [0] * P # 정류장 갯수(P)만큼 리스트를 생성
    for n in range(N):
        for idx, C in enumerate(C_list):
            if ab_list[n][0] <= C and ab_list[n][1] >= C:
                cnt_busline[idx] += 1

    print(f'#{test}', *cnt_busline)
