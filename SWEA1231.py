# SWEA 1231 중위순회

def inorder(n):
    global word
    if n:
        inorder(ch1[n])
        word += char[n]
        inorder(ch2[n])


for test in range(1, 11):
    N = int(input())
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    char = [0] * (N+1)
    for _ in range(N):
        lst = list(input().split())
        char[int(lst[0])] = lst[1]
        if len(lst) == 3:
            ch1[int(lst[0])] = int(lst[2])
        elif len(lst) == 4:
            ch1[int(lst[0])] = int(lst[2])
            ch2[int(lst[0])] = int(lst[3])

    # print(ch1)
    # print(ch2)
    # print(char)
    word = ''
    inorder(1)
    print(f'#{test} {word}')