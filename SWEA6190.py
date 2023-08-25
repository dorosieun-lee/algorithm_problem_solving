# SWEA 6190 정곤이의 단조 증가하는 수
# 효율 중요!

# 정곤이는 엄청난 수학자
# 단조 증가하는 수: 각 숫자의 자릿수가 단순하게 증가하는 수
# 자릿수가 오름차순이면 단조 증가하는 수, 단, 같아도 됨
# 단조 증가하는 수 중 최댓값 출력

def check_num(num):
    digit = [0]*len(str(num))
    n = len(str(num)) - 1
    while num >= 10:
        digit[n] = num % 10
        num //= 10
        n -= 1
    digit[n] = num
    if digit == sorted(digit):
        return True
    else:
        return False


T = int(input())
for test in range(1, T+1):
    N = int(input())
    A_list = sorted(list(map(int, input().split())), reverse=True) # 내림차순 정렬

    MAX = 0
    for i in range(N):
        for j in range(i+1, N):
            num = A_list[i] * A_list[j]
            if MAX < num and check_num(num):
                MAX = max(num, MAX)

    if MAX == 0:
        result = -1
    else:
        result = MAX

    print(f'#{test} {result}')