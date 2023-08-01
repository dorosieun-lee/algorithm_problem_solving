# SWEA 1244 최대 상금 -> 15개 테스트 케이스 중 5개 통과 못함
# 6번 테스트 케이스와 관련된 것으로 생각됨
T = int(input())

for test in range(1, T+1):
    N, cnt = list(input().split())
    cnt = int(cnt)
    num_list = list(map(int, N))

    if num_list.count(max(num_list)) == cnt:
        change_cnt = cnt

    else:
        change_cnt = 0

    for i in range(len(num_list)):
        if change_cnt >= cnt:
            break

        max_idx = len(num_list) - num_list[::-1].index(max(num_list[i:])) - 1
        if i == max_idx:
            continue
        else:
            num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]
            change_cnt += 1

    if (cnt - change_cnt) % 2 == 0: # 짝수면 왔다갔다 했다 치고 답은 변하지 않음
        pass

    else: # 홀수면....? 왔다갔다하고 한번이 남는다. 그때는 가장 뒤의 숫자 두개를 바꾸는게 영향이 가장 적음
        num_list[-1], num_list[-2] = num_list[-2], num_list[-1]

    max_number = int(''.join(list(map(str, num_list))))

    print(f'#{test} {max_number}')

