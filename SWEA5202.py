# SWEA 5202 화물 도크
# 활동 선택(Activity-selection) 문제

T = int(input())
for test in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    times.sort(key=lambda x: x[1]) # 종료시간 기준으로 오름차순 정렬
    #print(times)

    cnt = 0
    end = 0
    for s, e in times:
        if s >= end: # 종료시간보다 시작시간이 같거나 크면
            cnt += 1 # 화물차 사용 대수 +1
            end = e # 종료시간 변경

    print(f'#{test} {cnt}')