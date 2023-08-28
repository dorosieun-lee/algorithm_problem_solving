# A형 기출
def adj_cell(N):
    if N%W == 0: # 가장 오른쪽
        if W%2 == 0: # 짝수 너비
            lst = [N - W, N - 1, N + W - 1, N + W]
        else: # 홀수 너비
            lst = [N - W - 1, N - W, N - 1, N + W]
    elif (N%W)%2 != 0: # (가운데 수)를 가로 길이로 나눈 나머지가 홀수
        lst = [N - W - 1, N - W, N - W + 1, N - 1, N + W, N + 1]
        if (N%W) == 1:
            lst.remove(N-1)
            lst.remove(N-W-1)
    else: # (가운데 수)를 가로 길이로 나눈 나머지가 홀수
        lst = [N - W, N - 1, N + 1, N + W - 1, N + W, N + W + 1]

    for l in lst: # 음수와 범위 넘어가는 수 제거
        if l < 1 or l > W * H: lst.remove(l)
    return lst


def DFS(n, i, cells):
    if i == 4:
        for lst in my_lst:
            if set(cells) == set(lst):
                return
        else:
            my_lst.append(cells)
            return
    if n == min_cell:
        return

    else:
        adj_list = adj_cell(n)
        for a in adj_list:
            if (1 <= a <= W*H) and not visited[a]:
                visited[a] = True
                DFS(a, i+1, cells+[a])
                visited[a] = False



T = int(input())
for test in range(1, T+1):
    W, H = map(int, input().split())
    Users = []
    cell_numbers = []
    for h in range(H):
        cell_numbers.extend(list(range(h*W+1, (h+1)*W+1)))
        Users.extend(list(map(int, input().split())))
    # print(cell_numbers)
    # print(Users[cell_numbers.index(1)])
    min_cell = cell_numbers[Users.index(min(Users))]

    my_lst = []
    for N in cell_numbers:
        visited = [False] * (W * H + 1)
        visited[N] = True
        DFS(N, 1, [N])
        if (2 <= N%W) and (N+W <= W*H):
            my_lst.append([N-1, N, N+1, N+W])
        if (2 <= N%W) and ((N-W) >= 1) and (N+W+1 <= W*H):
            my_lst.append([N-W, N, N+W-1, N+W+1])


    MAX = 0
    for tmp in my_lst:
        cb = 0
        for c in tmp:
            cb += Users[cell_numbers.index(c)]
        cb = cb**2
        MAX = max(cb, MAX)

    # 인접 여부를 다 표시하거나 알 수 있는 규칙을 찾고
    # 기지국 놓기 완전탐색

    print(f'#{test} {MAX}')
