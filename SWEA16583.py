# SWEA 16583 토너먼트 카드게임
# [1,2] == [2,1] => False
T = int(input())


# 가위바위보를 하자 -> 이긴 학생의 인덱스를 반환
def fight(a, b):
    if set([lst[a], lst[b]]) == set([1, 2]):
        if lst[a] == 2:
            return a
        else:
            return b
    elif set([lst[a], lst[b]]) == set([1, 3]):
        if lst[a] == 1:
            return a
        else:
            return b
    elif set([lst[a], lst[b]]) == set([2, 3]):
        if lst[a] == 3:
            return a
        else:
            return b
    else: # 비긴 경우 -> 더 낮은 인덱스를 반환
        return min(a, b)


# 토너먼트해서 가장 밑단의 승자들을 추려냄
def div(i, j):
    # print(i,j)
    if i == j:
        return i
    elif j - i == 1:
        return fight(i, j)
    else:
        mid = (i+j)//2
        win1 = div(i, mid)
        win2 = div(mid+1, j)
        return fight(win1, win2)


for test in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    result = div(0, N-1)

    print(f'#{test} {result+1}')