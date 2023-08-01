# SWEA 1244 최대 상금 -> 15개 테스트 케이스 중 1개 통과 못함
# 번 테스트 케이스 다시 생각해야함 -> 아래 코드로는 88823이 나옴
# 교환가능한 숫자들과 인덱스의 리스트를 만들어서 조합하는 식으로 해보자!

T = int(input())

for test in range(1, T+1):
    N, cnt = list(input().split())
    cnt = int(cnt)
    num_list = list(map(int, N))

    if num_list.count(max(num_list)) == len(num_list): # 자릿수가 모두 같으면, 바꾸는게 무의미함
        change_cnt = cnt

    else:
        change_cnt = 0

    for i in range(len(num_list)):
        if change_cnt >= cnt:
            break

        max_idx = len(num_list) - num_list[::-1].index(max(num_list[i:])) - 1 # 최댓값이 있는 인덱스를 찾는데, 여러개 있으면 가장 오른쪽의 인덱스를 찾음
        if i == max_idx:
            continue
        else:
            num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]
            change_cnt += 1

    if change_cnt >= cnt:
        pass

    elif (cnt - change_cnt) % 2 == 0: # 짝수면 왔다갔다 했다 치고 답은 변하지 않음
        pass

    elif len(set(num_list)) < len(num_list): # num_list 내부에 같은 수가 있으면 그 안에서 서로 왔다갔다하면 됨
        pass

    elif (cnt - change_cnt) % 2 == 1: # cnt - change_cnt 갸 홀수면 왔다갔다하고 한번이 남는다. 그때는 가장 뒤의 숫자 두개를 바꾸는게 영향이 가장 적음
        num_list[-1], num_list[-2] = num_list[-2], num_list[-1]

    max_number = int(''.join(list(map(str, num_list))))

    print(f'#{test} {max_number}')

