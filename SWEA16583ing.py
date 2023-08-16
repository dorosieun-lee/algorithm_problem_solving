# SWEA 16583 토너먼트 카드게임
# 런타임 에러
# 4 <= N <= 100 이므로 시간초과는 아님
# 그럼 인덱스 에러..?
T = int(input())


# 가위바위보를 하자 -> 이긴 학생의 인덱스를 반환
def fight(a, b):
    if [lst[a], lst[b]] == [1, 2]:
        if lst[a] == 2:
            return a
        else:
            return b
    elif [lst[a], lst[b]] == [1, 3]:
        if lst[a] == 1:
            return a
        else:
            return b
    elif [lst[a], lst[b]] == [2, 3]:
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
        winners.append(div(i, mid))
        winners.append(div(mid+1, j))


for test in range(1, 2): #T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    winners = []
    div(0, N-1)
    print(winners)
    while None in winners:
        winners.remove(None)
    while len(winners) >= 2:
        new_winners = []
        for i in range(0, len(winners), 2):
            new_winners.append(fight(winners[i], winners[i+1]))
        winners = new_winners

    print(f'#{test} {winners[0] + 1}')