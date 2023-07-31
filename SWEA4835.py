T = int(input())

for test in range(1, T + 1):
    N, M = list(map(int, input().split()))
    num_list = list(map(int, input().split()))

    sub_sum = []
    for i in range(N - M + 1):
        sub_sum.append(sum(num_list[i:i + M]))
    # print(sub_sum)

    min_val = 10000 * M  # 조건에 의한 최대 부분합
    max_val = 0

    for num in sub_sum:
        if min_val > num:
            min_val = num
        if max_val < num:
            max_val = num

    diff = max_val - min_val
    print(f'#{test} {diff}')