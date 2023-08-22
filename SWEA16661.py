# SWEA 16661 이진 힙

def change(ch): # 자식 노드의 값 < 부모 노드의 값 이면 자식노드, 부모 노드 자리 바꾸는 함수
    if ch == 1: # 루트 노드이면,
        return

    if ch in ch1:
        p = ch1.index(ch)
    else:
        p = ch2.index(ch)

    if new_list[ch] < new_list[p]: # 자식 노드의 값 < 부모 노드의 값
        new_list[ch], new_list[p] = new_list[p], new_list[ch] # 자리 바꾸기
        change(p)


T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    # 포화 이진 트리 만듦
    ch1 = [2*i for i in range(N//2+1)] # 왼쪽 자식 노드 = 노드 번호가 짝수
    ch2 = [2*i+1 for i in range(N//2+1)] # 오른쪽 자식 노드 = 노드 번호가 홀수
    new_list = [0] * (N+1) # 트리에 저장되는 값을 담은 리스트
    new_list[1] = lst[0] # 첫번째 값을 루트노드에 담고 시작

    idx = 1
    # 포화 이진 트리 채우기
    for i in range(1, N//2+1): # i는 자식노드에 해당하는 리스트의 크기와 일치
        new_list[ch1[i]] = lst[idx] # 왼쪽 자식노드부터 먼저 채우고
        change(ch1[i]) # 문제 조건에 맞게 자리 바꾸고
        idx += 1

        if idx == N: # lst의 끝에 도달하면 for문 나가기
            break

        new_list[ch2[i]] = lst[idx] # 오른쪽 자식 노드 채우고
        change(ch2[i])
        idx += 1

        if idx == N:
            break


    total = 0
    idx2 = N
    # 조상을 찾자~
    while True:
        if idx2 == 1: # 루트에 갔으면,
            break

        if idx2 in ch1:
            tmp = ch1.index(idx2)
            total += new_list[tmp]
            idx2 = tmp
        elif idx2 in ch2:
            tmp = ch2.index(idx2)
            total += new_list[tmp]
            idx2 = tmp

    print(f'#{test} {total}')