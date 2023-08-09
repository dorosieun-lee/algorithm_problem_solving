# 프로그래머스 소수 만들기
# 주어진 숫자 리스트에서 3개의 요소를 가지는 부분집합을 찾아서 그 합이 소수인게 몇 개인지 찾기
def solution(nums):
    cnt = 0
    subset = []
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                tmp = [nums[i], nums[j], nums[k]]
                if tmp not in subset:
                    subset.append(tmp)
                    if is_prime(sum(tmp)):
                        cnt += 1

    return cnt


def is_prime(number):
    print(number)
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


nums =[1,2,3,4]
print(solution(nums))