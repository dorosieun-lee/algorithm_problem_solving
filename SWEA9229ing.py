# SWEA 9229 한빈이와 spot mart
# 제시된 테스트 케이스는 통과
# 파이썬 언어 지원을 안함;;; 언젠가.. 자바로 바꿔보자...

# 정확히 과자 두 봉지~~
# N개의 과자 봉지
# 과자 봉지는 ai그램의 무게
# M 그램 초과하면 안됨
# 최대 무게 합 출력!

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split()) # 과자 봉지의 개수, 무게 합
    weight = list(map(int, input().split())) # N개 과장 봉지의 무게

    weight.sort() # 일단 정렬!
    if weight[0] + weight[1] > M:
        flag = False

    else:
        flag = False
        MAX = 0
        for i in range(N):
            for j in range(i, N):
                total = weight[i] + weight[j]
                if total == M:
                    flag = True
                    MAX = M
                    break
                if total < M:
                    MAX = max(total, MAX)
                    flag = True
            if MAX == M:
                break

    if not flag:
        MAX = -1

    print(f'#{test} {MAX}')