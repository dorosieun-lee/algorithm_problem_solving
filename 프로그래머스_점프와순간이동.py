# 프로그래머스 점프와 순간이동

# 순간이동 시(현재까지 온 거리 X 2) 건전지 사용량이 줄지 않음
# K칸을 점프하면 K 만큼의 건전지 사용량이 듬
# 순간이동을 하는 것이 더효율적

# N 만큼 떨어진 장소로 가려고 할때, 건전지 사용량의 최솟값을 구하라


def solution(N):
    memo = [0] * (N+1)
    memo[1], memo[2] = 1, 1

    for n in range(1, N+1):
        if memo[n] == 0:
            if n % 2 != 0: # n이 홀수면
                memo[n] = 1 + memo[n-1]
            else:
                memo[n] = memo[n//2]

    return memo[N]

def solution(N):
    ans = 1
    while N > 1:
        if N % 2 != 0:
            ans += 1
            N = (N-1) // 2
        else:
            N = N // 2
    return ans


N = 5000
print(solution(N))