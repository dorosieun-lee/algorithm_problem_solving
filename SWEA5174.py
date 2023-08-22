# SWEA 5174 subtree

def find_node(n):
    global cnt
    if ch1[n]:
        cnt += 1
        find_node(ch1[n])
    if ch2[n]:
        cnt += 1
        find_node(ch2[n])

T = int(input())

for test in range(1, T+1):
    E, N = map(int, input().split()) # 간선의 개수, 서브트리의 루트 노드
    edges = list(map(int, input().split()))
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)

    for i in range(E):
        p, c = edges[i*2], edges[i*2 + 1]
        if ch1[p]:
            ch2[p] = c
        else:
            ch1[p] = c

    cnt = 1
    find_node(N)

    print(f'#{test} {cnt}')
