N, M = map(int, input().split())

row_check = [0] * N
col_check = [0] * M


for n in range(N):
    row = list(input())
    idx = 0
    # 각 행에서 X가 몇 번째 열에 있는지 체크해서 해당 인덱스의 col_check 값 1 증가
    for r in row:
        if r == 'X':
            col_check[idx] += 1
        idx += 1

    # 각 행에 X가 있으면 해당하는 행 인덱스의 row_check 값 1 증가
    if row.count('X') >= 1:
        row_check[n] += 1

print(max(col_check.count(0), row_check.count(0)))
