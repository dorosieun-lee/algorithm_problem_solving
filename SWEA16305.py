# SWEA 16305 특별한 정렬
T = int(input())

for test in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(0, 10):
        if i % 2 == 0: # 짝수 인덱스 -> max
            max_idx = i
            for j in range(i, N):
                if lst[max_idx] < lst[j]:
                    max_idx = j
            lst[i], lst[max_idx] = lst[max_idx], lst[i]

        else:
            min_idx = i
            for j in range(i, N):
                if lst[min_idx] > lst[j]:
                    min_idx = j
            lst[i], lst[min_idx] = lst[min_idx], lst[i]


    print(f'#{test}',*lst[:10])