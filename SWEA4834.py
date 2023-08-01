# SWEA 4834 숫자 카드
T = int(input())

for test in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))

    counts = [0] * 10 # 0부터 9까지의 리스트 생성(개수 세기용)
    for i in cards:
        counts[i] += 1

    max_cnt = max(counts)
    for i, cnt in enumerate(counts[::-1]):
        if cnt == max_cnt:
            max_value = 9 - i # 장수가 같다면 숫자가 큰 쪽을 출력하기 위해서 뒤에서부터 순회
            break

    print(f'#{test} {max_value} {max_cnt}')