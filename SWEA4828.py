T = int(input())

for test in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    min_val, max_val = 9999999, -9999999
    for num in num_list:
        if max_val < num:
            max_val = num
        if min_val > num:
            min_val = num

    diff = max_val - min_val

    print(f'#{test+1} {diff}')