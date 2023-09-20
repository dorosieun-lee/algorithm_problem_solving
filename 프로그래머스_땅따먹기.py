def solution(land):
    for row in range(1, len(land)):
        for c in range(4):
            tmp = land[row-1][:]
            del tmp[c]
            land[row][c] += max(tmp)

    print(land)
    return max(land[-1])