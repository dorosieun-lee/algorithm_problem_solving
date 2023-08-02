# SWEA 1244 최대 상금
# 단순화 시켜볼 것

T = int(input())

for test in range(1, T+1):
    N, cnt = list(input().split())
    cnt = int(cnt)
    num_list = list(map(int, N))

    if num_list.count(max(num_list)) == len(num_list): # 자릿수가 모두 같으면, 바꾸는게 무의미함
        change_cnt = cnt
    else:
        change_cnt = 0

    sorted_list = sorted(num_list) # 오름차순
    #print(sorted_list)
    for i in range(len(num_list)):
        if change_cnt == cnt or num_list == sorted_list[::-1]:
            break

        if num_list[i:].count(max(num_list[i:])) == 1:
            max_idx = num_list[i:].index(max(num_list[i:])) + i
            if max_idx == i:
                continue
            else:
                num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]
                change_cnt += 1
                #print('a', change_cnt, num_list) # 어디에서 자릿수가 바뀌는지 확인하기 위함

        else:
            max_idx_list = [] # max index 저장하는 list
            for j in range(len(num_list)):
                if num_list[j] == max(num_list[i:]):
                    max_idx_list.append(j)

            sorted_idx = sorted_list.index(num_list[i]) # 바꾸고자하는 수가 뒤에서 몇 번째로 큰 수인지 체크

            if sorted_idx+1 <= len(max_idx_list):
                max_idx = max_idx_list[::-1][sorted_idx] # max 숫자가 있는 인덱스들 중 바꾸고자하는 수의 순서에 해당하는 max index 찾기
                num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]
                change_cnt += 1
                #print('b', change_cnt, num_list)
            else:
                max_idx = max_idx_list[0]
                num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]
                change_cnt += 1
                #print('c', change_cnt, num_list)

    if (cnt - change_cnt) % 2 == 0: # 짝수면 왔다갔다 했다 치고 답은 변하지 않음
        pass
    elif len(set(num_list)) < len(num_list): # num_list 내부에 같은 수가 있으면 그 안에서 서로 왔다갔다하면 됨
        pass
    elif (cnt - change_cnt) % 2 == 1: # cnt - change_cnt 가 홀수면 왔다갔다하고 한번이 남는다. 그때는 가장 뒤의 숫자 두개를 바꾸는게 영향이 가장 적음
        num_list[-1], num_list[-2] = num_list[-2], num_list[-1]

    max_number = int(''.join(list(map(str, num_list))))

    print(f'#{test} {max_number}')