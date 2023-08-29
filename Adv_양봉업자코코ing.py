# Adv 양봉업자 코코
# 일부 정답
def adj_cell(N):
    if N % W == 0:  # 가장 오른쪽
        if W % 2 == 0:  # 짝수 너비
            lst = [N - W, N - 1, N + W - 1, N + W]
        else:  # 홀수 너비
            lst = [N - W - 1, N - W, N - 1, N + W]
    elif (N % W) % 2 != 0:  # (가운데 수)를 가로 길이로 나눈 나머지가 홀수
        lst = [N - W - 1, N - W, N - W + 1, N - 1, N + W, N + 1]
        if (N % W) == 1:
            lst.remove(N - 1)
            lst.remove(N - W - 1)
    else:  # (가운데 수)를 가로 길이로 나눈 나머지가 홀수
        lst = [N - W, N - 1, N + 1, N + W - 1, N + W, N + W + 1]

    for l in lst:  # 음수와 범위 넘어가는 수 제거
        if l < 1 or l > W * H: lst.remove(l)
    return lst


def DFS(n, i, cells):
    if i == 4:
        my_lst.append(cells)
        return

    adj_list = adj_cell(n)
    for a in adj_list:
        if 1 <= a <= W * H and not visited[a]:
            visited[a] = True
            DFS(a, i + 1, cells + [a])
            visited[a] = False


T = int(input())
for test in range(1, T + 1):
    H, W = map(int, input().split())
    honey = []
    cell_numbers = []

    for h in range(H):
        cell_numbers.extend(list(range(h * W + 1, (h + 1) * W + 1)))
        honey.extend(list(map(int, input().split())))

    my_lst = []

    visited = [False] * (W * H + 1)
    for N in cell_numbers:
        visited[N] = True
        DFS(N, 1, [N])
        visited[N] = False

        if 2 <= N % W and N + W <= W * H:
            if (N % W) % 2 == 0: # 짝수 열
                my_lst.append([N - 1, N, N + 1, N + W])
            elif (N % W) % 2 == 1: # 홀수 열
                my_lst.append([N - W - 1, N, N + W + 1, N + W])

        if 2 <= N % W and N - W >= 1:
            if (N % W) % 2 == 0 and N + W + 1 <= W * H: # 짝수 열
                my_lst.append([N - W, N, N + W - 1, N + W + 1])
            elif (N % W) % 2 == 1:  # 홀수 열
                my_lst.append([N - W, N, N - 1, N + 1])

    MAX = 0
    for tmp in my_lst:
        cb = sum(honey[c - 1] for c in tmp)
        MAX = max(cb, MAX)

    print(f'#{test} {MAX}')