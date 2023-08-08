# SWEA 1221 GNS
T = int(input())

order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for test in range(1, T+1):
    input()
    lst = input().split()

    new_lst = []
    for o in order:
        for s in lst:
            if s == o:
                new_lst.append(s)

    print(f'#{test}')
    print(*new_lst)





