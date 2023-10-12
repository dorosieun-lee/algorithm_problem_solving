# 프로그래머스 2xn 타일링

# SWEA 문제는 리스트 만들어도 시간 초과 안났는데 얘는 났음...
# 리스트 안 쓰고 변수만 사용하는게 팁이었음!
def solution(n):
    num1 = 1
    num2 = 1

    if n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            num1 = num1 + num2
            num1, num2 = num2, num1

    return num2 % 1000000007