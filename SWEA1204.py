# SWEA 1204 최빈수 구하기

T = int(input())

for test in range(1, T+1):
    N_case = int(input())
    numbers = list(map(int, input().split()))
    counts = [0] * (max(numbers) + 1)
    for n in numbers:
        counts[n] += 1

    # 최빈수가 여러 개일 때에는 가장 큰 점수를 출력하기 위해서
    # counts 뒤에서부터 max index를 찾고 max number에서 빼주는 방식으로 구함
    max_val = max(numbers) - counts[::-1].index(max(counts))

    print(f'#{N_case} {max_val}')