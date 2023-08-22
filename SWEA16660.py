# SWEA 16660 노드의 합
# 완전 이진 트리

T = int(input())
for test in range(1, T+1):
    N, M, L = map(int, input().split()) # 노드의 개수, 리프 노드의 개수, 값을 출력할 노드 번호
    ch1 = [i*2 for i in range(N//2+1)] # 완전 이진 트리 구조 만들기
    ch2 = [i*2+1 for i in range(N//2+1)]

    lst = [0] * ((N//2+1)*2) # 값이 저장되는 리스트
    for _ in range(M):
        idx, val = map(int, input().split())
        lst[idx] = val # 주어진 리프 노드의 값을 저장

    # 자식 노드의 값을 합쳐서 부모 노드에 저장
    for i in range(len(ch1)-1, 0, -1):
        val = lst[ch1[i]] + lst[ch2[i]]
        #print(i, val)
        lst[i] = val

    print(f'#{test} {lst[L]}')