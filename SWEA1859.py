# SWEA 1859

# 원재는 미래를 보는 능력을 갖게 되었다.
# 원재를 사재기를 하려고 한다. 당국의 감시를 피해서

# 1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
# 2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
# 3. 판매는 얼마든지 할 수 있다.

# 1번째 케이스는 아무것도 사지 않는 것이 최대 이익이다
# 2번째 케이스는 1,2일에 각각 한 개씩 사서 세 번째 날에 두 개를 팔면 10의 이익을 얻을 수 있다
# 1번째 -> 10 7 6
# 2번째 -> 3 5 9 -> (9 - 3) + (9 - 5) = 6 + 4 = 10

# 전 날의 가격보다 다음 날의 가격이 비싸면 이득을 볼 수 있음.
# 최대 이익을 보려면, 가장 비싼 날에 팔아야함
# 일단 이익이 되는지 판단하고 이익을 계산
#
def find_max_benefit(my_list):
    #print(my_list)
    max_idx = my_list.index(max(my_list))
    if len(my_list) == 1: # 재귀함수 종료 케이스
        return 0
    else:
        result = 0
        for i, num in enumerate(my_list):
            if i == max_idx: # 자기 자신이 가격이 최대이면, 반복문에서 종료
                break
            else:
                result += (my_list[max_idx] - num) # 최댓값과 리스트 내 각 요소의 차이를 result에 더함
        #print(result)
        if max(my_list) != my_list[-1]:
            return result + find_max_benefit(my_list[max_idx+1:]) # 위에서 구한 최대 이익 + max_idx 뒤의 리스트에서의 최대 이익
        else:
            return result

T = int(input()) # 테스트 케이스의 수

for test in range(T):
    N = int(input()) # 연속된 N일에 해당하는 N
    my_list = list(map(int, input().split())) # 각 날의 매매가, 10000이하
    max_idx = my_list.index(max(my_list))
    if max_idx == 0:
        max_benefit = 0
    else:
        max_benefit = find_max_benefit(my_list)

    print(f'#{test+1} {max_benefit}')

# 10개의 케이스 중 7개는 통과, 3개에서 runtime error남