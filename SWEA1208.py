# SWEA1208

T = 10 # test case 횟수

# min, max index를 찾아서 +1, -1 해줌
for test in range(1, T+1):
    N_dump = int(input())
    box_list = list(map(int, input().split()))

    for n in range(N_dump):
        max_idx = box_list.index(max(box_list))
        min_idx = box_list.index(min(box_list))
        box_list[max_idx] -= 1
        box_list[min_idx] += 1

    max_diff = max(box_list) - min(box_list)

    print(f'#{test} {max_diff}')

# sorted 내장함수를 이용
for test in range(1, T+1):
    N_dump = int(input())
    box_list = sorted(list(map(int, input().split()))) # sorted:

    for n in range(N_dump):
        box_list[0] += 1
        box_list[-1] -= 1
        box_list = sorted(box_list)

    max_diff = box_list[0] - box_list[-1]

    print(f'#{test} {max_diff}')