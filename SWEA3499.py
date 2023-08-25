# SWEA 3499 퍼펙트 셔플

T = int(input())
for test in range(1, T+1):
    N = int(input()) # 카드 개수
    deck = input().split()

    deckA = deck[:(N+1)//2]
    deckB = deck[(N+1)//2:]
    new_deck = []
    for i in range(N//2):
        new_deck.append(deckA[i])
        new_deck.append(deckB[i])

    if i < len(deckA)-1:
        new_deck.append(deckA[-1])

    print(f"#{test} {' '.join(new_deck)}")