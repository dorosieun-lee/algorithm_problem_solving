# SWEA 5248 그룹 나누기

"""
아래 코드는 10개 테케 중 3개만 맞음
이유 모르겠음

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    pairs = []
    for i in range(0, M*2, 2):
        for pair in pairs:
            if numbers[i] in pair:
                pair.append(numbers[i+1])
                break
            if numbers[i+1] in pair:
                pair.append(numbers[i])
                break
        else:
            pairs.append(list(numbers[i:i+2]))

    remain = set(range(1, N+1)) - set(numbers)
    result = len(pairs) + len(remain)
    print(f'#{test} {result}')

"""

def BFS(start):
    global visited
    visited[start] = True
    queue = [start]

    while queue:
        n = queue.pop()
        for w in adj_list[n]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True


T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    adj_list = [[] for _ in range(N+1)]
    for i in range(0, M*2, 2):
        adj_list[numbers[i]].append(numbers[i+1])
        adj_list[numbers[i+1]].append(numbers[i])

    cnt = 0
    visited = [False] * (N + 1)
    for n in range(1, N+1):
        if not visited[n]:
            cnt += 1
            BFS(n)

    print(f'#{test} {cnt}')
