# SWEA 4408 자기 방으로 돌아가기

# 인덱스 처리와 방의 형식, 항상 작은 번호 -> 큰 번호가 아니라는 점에 주의하기.
T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = [sorted(list(map(int, input().split()))) for _ in range(N)]

    room = [0] * 201

    for i in range(N):
        start = (lst[i][0]+1)//2
        end = (lst[i][1]+1)//2
        for j in range(start, end+1):
            room[j] += 1

    result = max(room)
    print(f'#{test} {result}')


