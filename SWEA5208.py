# SWEA 5208 전기버스2

# 최소한의 충전지 교체 횟수

def move(index, cnt):
    global MIN
    if index > N-2:
        MIN = min(cnt, MIN)
        return
    if cnt >= MIN:
        return

    for b in range(1, M[index]+1):
        move(index+b, cnt+1)


T = int(input())
for test in range(1, T+1):
    line = list(map(int, input().split()))
    N = line[0] # 정류장 개수
    M = line[1:] # 정류장 별 배터리 용량 -> N-1개

    MIN = float("inf")
    move(0, 0)

    print(f'#{test} {MIN-1}')

