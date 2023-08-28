# SWEA 16811 당근 포장하기

# N개의 당근을 대, 중, 소 상자로 구분해 포장
# 같은 크기의 당근은 같은 상자에 들어가야함
# 비어 있는 상자는 없다
# 한 상자에 int(N/2) 개를 초과하는 당근이 있으면 안됨
# 각 상자에 든 당근의 개수 차이가 최소가 되도록

# index로 구간 나누기
T = int(input())
for test in range(1, T+1):
    N = int(input())
    carrot = sorted(list(map(int, input().split())))
    min_v = 1000
    for i in range(N-2):
        for j in range(i+1, N-1):
            if carrot[i] != carrot[i+1] and carrot[j] != carrot[j+1]:
                small = i+1
                mid = j-i
                large = N-1 - j
                if 0 < small <= int(N/2) and 0 < mid <= int(N/2) and 0 < large <= int(N/2):
                    if max([small, mid, large]) - min([small, mid, large]) < min_v:
                        min_v = max([small, mid, large]) - min([small, mid, large])

    if min_v == 1000:
        result = -1
    else:
        result = min_v

    print(f'#{test} {result}')
