# SWEA 4831 전기버스

T = int(input())

for test in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    station_idx = list(map(int, input().split()))

    station_list = [0] * N
    for s in station_idx:
        station_list[s] = 1
    #print(station_list)
    cnt = 0
    cnt_charge = 0
    i = 0
    is_error = False
    while i < (N-1):
        cnt += 1
        i += 1
        if cnt == K: # 최대로 갈 수 있는 칸을 가서
            if station_list[i] == 1: # 충전소가 있는지 확인
                cnt_charge += 1 # 있으면 충전 횟수 +1하고 다시 반복함
                cnt = 0 # cnt 리셋
                continue
            else: # 충전소가 없으면, 충전소가 나올 때까지 뒷걸음질
                back = 0
                while True:
                    i -= 1
                    back += 1
                    if back == K: # K번 뒷걸음질 했는데 충전 못함 -> 설치가 잘못 되었음 -> 0을 출력 (아래에서 처리)
                        is_error = True
                        break
                    if station_list[i] == 1:
                        cnt_charge += 1
                        cnt = 0
                        break # 충전하면 break


    if is_error:
        print(f'#{test} 0')
    else:
        print(f'#{test} {cnt_charge}')