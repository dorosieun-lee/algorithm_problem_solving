# SWEA 1219 길찾기

# 방향성이 있고, 갈림길은 최대 2개
# 길 존재: 1, 존재X : 0

def dfs(start, end, nodes, adj_dict):
    stack = [start]
    visited = [0] * nodes
    visited[start] = 1
    n = start
    while True:
        if n == end:
            return 1

        for w in adj_dict[n]:
            if visited[w] == 0:
                n = w
                stack.append(n)
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break

    if visited[end] == 1:
        return 1
    else:
        return 0

while True:
    try:
        tc, N = list(map(int, input().split()))
        path = list(map(int, input().split()))
    except:
        break

    adj_dict = {i: [] for i in range(100)}

    for i in range(N):
        start = path[i*2]
        end = path[i*2+1]
        adj_dict[start].append(end)

    print(f'#{tc} {dfs(0, 99, 100, adj_dict)}')