# SWEA 11092 최대 최소의 간격
# 최대값의 위치는 뒤 기준
# 최소값의 위치는 앞 기준

T = int(input())

for test in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    min_idx = 0 # 최소값의 인덱스
    max_idx = 0 # 최대값의 인덱스
    for i in range(1, N):
        if num_list[min_idx] > num_list[i]: # 등호가 없으면, 같은 수 중 가장 왼쪽 인덱스가 저장됨
            min_idx = i
        if num_list[max_idx] <= num_list[i]: # 등호를 넣으면, 같은 수 중 가장 오른쪽 인덱스가 저장됨
            max_idx = i
    #print(min_idx)
    #print(max_idx)

    if min_idx > max_idx:
        diff = min_idx - max_idx
    else:
        diff = max_idx - min_idx

    print(f'#{test} {diff}')