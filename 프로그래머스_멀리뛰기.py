# 프로그래머스 멀리뛰기
# DP 문제가 확실합니다!
# 두 함수 모두 가능

def solution1(n):
    lst = [0, 1, 2] + [0] * (n-2)
    if n > 2:
        for i in range(3, n+1):
            lst[i] = lst[i-1] + lst[i-2]
    return lst[n] % 1234567


def solution2(n):
    a, b = 1, 2
    if n == 1:
        return 1

    for i in range(2, n):
        a, b = b, a+b
    return b % 1234567


n = 200000
import time
start = time.time()
print(solution1(n))
print(f"time : {time.time() - start: 0.10f}") # -> time :  4.5404942036

start = time.time()
print(solution2(n))
print(f"time : {time.time() - start: 0.10f}") # -> time :  0.5779900551

# 반복문 안도는 solution2가 약 9배 빠름..!