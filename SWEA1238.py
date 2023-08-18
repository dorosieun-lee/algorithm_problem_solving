# SWEA 1238 contact
# 방향이 있는 그래프

def BFS(S):
    is_contact[S] = 1
    queue = [S]

    while queue:
        n = queue.pop(0)
        for w in adj_list[n]:
            if is_contact[w] == 0: # 연락한 적 없는 사람이면
                queue.append(w) # 일단 큐에 다 넣어라
                is_contact[w] = is_contact[n] + 1 # 연락이 가는데까지 필요했던 연락 횟수를 표시


for test in range(1, 11):
    L, S = list(map(int, input().split())) # 입력받는 데이터의 길이, 시작점
    contact_list = list(map(int, input().split())) # from, to, from, to, ..

    is_contact = [0] * 101  # 연락 인원은 최대 100명
    adj_list = [[] for _ in range(101)]
    for i in range(0, L, 2):
        adj_list[contact_list[i]].append(contact_list[i+1])

    BFS(S)
    idx = 100 - is_contact[::-1].index(max(is_contact))
    # 가장 마지막에 연락 받은 사람 중 숫자가 큰 사람 반환해야하므로 뒤에서부터 찾고 100에서 그 수를 빼줌

    print(f'#{test} {idx}')