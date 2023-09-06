# 프로그래머스 다음 큰 숫자

# 이진수로 변환했을 때, n과 1의 개수가 같고 n보다는 큰 수인 가장 작은 수 찾기
# 1의 개수가 같은 이진수 가능한거 다 만들어서
# n보다 크면서 가장 작은거 만들기?

def solution(n):
    n_bin = bin(n)[2:]
    cnt_one = n_bin.count('1')
    num = n+1
    while True:
        if bin(num).count('1') == cnt_one:
            break
        num += 1

    return num


n = 78
print(solution(n))
