# SWEA 18542 이진탐색
def inorder(n):
    if n: # n이 0이 아니면,
        inorder(ch1[n])
        lst.append(n)
        inorder(ch2[n])


T = int(input())
for test in range(1, T + 1):
    N = int(input())
    h = 0
    while 2 * (h + 1) - 1 <= N:
        h += 1

    lst = []
    # 1 - N 인덱스로 채워진 이진 트리를 만들고
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    for i in range(2, N+1):
        if i%2 == 0:
            ch1[i//2] = i
        else:
            ch2[i//2] = i

    # inorder로 순회하면서 lst 채우기(lst의 인덱스+1 이 노드 안의 숫자를 의미)
    inorder(1)

    print(f'#{test} {lst.index(1) + 1} {lst.index(int(N/2)) + 1}')