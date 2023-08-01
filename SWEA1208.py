# SWEA1208

T = 10 # test case 횟수

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