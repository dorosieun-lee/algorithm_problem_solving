# SWEA 4047 영준이의 카드 카운팅

T = int(input())

for test in range(1, T+1):
    S = list(range(1, 14))
    D = list(range(1, 14))
    H = list(range(1, 14))
    C = list(range(1, 14))
    deck = input() # string
    cards = [deck[i:i+3] for i in range(0, len(deck), 3)]

    if len(list(set(cards))) < len(cards): # 중복 있으면
        result = 'ERROR'
    else:
        for card in cards:
            if card[0] == 'S':
                S.remove(int(card[1:]))
            elif card[0] == 'D':
                D.remove(int(card[1:]))
            elif card[0] == 'H':
                H.remove(int(card[1:]))
            elif card[0] == 'C':
                C.remove(int(card[1:]))

        result = f'{len(S)} {len(D)} {len(H)} {len(C)}'

    print(f'#{test} {result}')
