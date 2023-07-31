T = int(input())


def do_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


for test in range(1, T+1):
    N = int(input()) # 5 이상 50 이하
    my_list = list(map(int, input().split()))
    new_list = do_sort(my_list)

    print(f'#{test}', *new_list)