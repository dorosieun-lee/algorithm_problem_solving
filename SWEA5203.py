# SWEA 5203 베이비진 게임
def check(deck):
    count = [0] * 10
    for d in deck:
        count[d] += 1

    # triplet 검사
    for n in [3, 4, 5, 6]:
        if count.count(n) >= 1:
            return True

    # run 검사
    cnt = 0
    for c in count:
        if c >= 1:
            cnt += 1
            if cnt == 3:
                return True
        else:
            cnt = 0
    return False



T = int(input())
for test in range(1, T+1):
    cards = list(map(int, input().split()))
    deck1 = []
    deck2 = []
    for i in range(len(cards)):
        if i%2 == 0:
            deck1.append(cards[i])
            if i >= 4:
                if check(deck1):
                    result = 1
                    break
        else:
            deck2.append(cards[i])
            if i >= 5:
                if check(deck2):
                    result = 2
                    break

    else:
        result = 0

    print(f'#{test} {result}')