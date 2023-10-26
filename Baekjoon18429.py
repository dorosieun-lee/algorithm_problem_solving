# 백준 18429 근손실
from itertools import permutations as perms

N, K = map(int, input().split())
my_lst = list(map(int, input().split()))

count = 0
# permutations 사용해서 가능한 경우의 수를 모두 살펴보는 것이 포인트
# for ... else 구문을 활용하면 is_pass를 쓰지 않아도 된다.
for lst in perms(my_lst, len(my_lst)):
    init = 500 # 중량 초기 상태
    is_pass = True
    for l in lst:
        init += (l - K)
        if init < 500:
            is_pass = False
            break
    if is_pass: count += 1

print(count)