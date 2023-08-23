# Beakjoon 2669 직사각형 네개의 합집합의 면적 구하기
# 네모 면적 다 더하고 겹치는거 빼주기 또는 이차원 배열에 다 배치해서 숫자 있는 칸 세기

MAP = [[0]*101 for _ in range(101)] # 101x101 이차원 배열
max_row = 0
max_col = 0
for _ in range(4):
    nemo = list(map(int, input().split()))
    for row in range(nemo[1], nemo[3]):
        for col in range(nemo[0], nemo[2]):
            MAP[row][col] += 1
            max_col = max(col, max_col)
            max_row = max(row, max_row)

cnt = 0

for row in range(0, max_row+1):
    for col in range(0, max_col+1):
        if MAP[row][col] != 0:
            cnt += 1

print(cnt)

