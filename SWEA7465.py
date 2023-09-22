# SWEA 7465 창용 마을 무리의 개수
# 그룹나누기 -> Union find 이용

def find_set(x):
    if parents[x] == x:
        return x

    return find_set(parents[x])


def union_set(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    return


T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    parents = [i for i in range(0, N+1)]

    for _ in range(M):
        x, y = map(int, input().split())
        union_set(x, y)

    # 서로 다른 부모가 몇 개인지 탐색!
    SET = set()
    for i in range(1, N+1):
        SET.add(find_set(i))
    result = len(SET)
    print(f'#{test} {result}')