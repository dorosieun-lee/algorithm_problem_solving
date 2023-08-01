# SWEA 연속한 1의 개수

T = int(input())

for test in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input()))
    # num_list = list(input()) 이렇게 쓰면 리스트 내의 인자가 문자열임.

    # 1의 인덱스가 담긴 리스트를 생성해서 연속된 수의 최대 길이를 구함
    idx_list = []
    for i in num_list:
        if i == 1:
            idx_list.append(i)

    cnt = 0
    cnt_list = []
    for i in num_list:
        if i == 1:
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 0
            continue
    cnt_list.append(cnt)
    print(f'#{test} {max(cnt_list)}')