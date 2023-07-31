T = 10 # test 갯수


for test in range(1, T+1):
    N = int(input()) # <= 1000
    height_list = list(map(int, input().split()))

    #print(N)
    #print(height_list)
    view_num = 0
    for i in range(N):
        sub = height_list[i:i+5] # 오른쪽, 왼쪽으로 2칸 이상 확보되어야 하므로 건물 5개씩 잘라서 생각함
        if len(sub) < 5: # 길이가 5 미만인 부분 리스트는 생각 안함
            continue

        max_idx = sub.index(max(sub))
        if max_idx == 2: # 가운데 건물이 가장 높으면 조망권 확보된 것
            min_val = 255 # max height
            for idx in range(5):
                if idx == 2:
                    continue
                else:
                    diff = sub[2] - sub[idx]
                    if min_val > diff:
                        min_val = diff

            view_num += min_val

    print(f'#{test} {view_num}')
