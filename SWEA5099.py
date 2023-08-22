# SWEA 5099 피자굽기
T = int(input())

for test in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    rot_pan = list(range(N)) # N 개의 피자받침에 첨에 꽉 채움
    idx = N # pizza 의 번호 - 1
    cheeze = [pizza[i] for i in range(N)] # 치즈 초기 세팅

    while True:
        for n in range(N): # 회전판 내 치즈 녹임
            cheeze[n] //= 2

        while 0 in cheeze: # 치즈가 다 녹은 판이 있는지 확인
            # 피자 새로 세팅
            rot_pan[cheeze.index(0)] = idx
            cheeze[cheeze.index(0)] = pizza[idx]
            idx += 1
            if idx == M: # 넣을 피자가 없는 경우
                break
        # print(idx)
        # print('pan:',rot_pan)
        # print('cheeze:',cheeze)
        if idx == M: # 피자 다 회전판에 넣었으면, while문 나가자
            break

    # 마지막 검사
    while set(cheeze) != set([0,1]): # cheeze 리스트에 0,1만 남을 때까지 구워!
        for n in range(N):
            cheeze[n] //= 2

    # print('pan:', rot_pan)
    # print('cheeze:', cheeze)
    last = rot_pan[::-1][cheeze[::-1].index(1)] + 1 # 1 중에서는 뒤에 위치한 애가 늦게 나옴

    print(f'#{test} {last}')

