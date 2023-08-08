# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다.
# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 시간초과 -> 실패
import sys
input = sys.stdin.readline

N = int(input())

my_list = []
# sort 알고리즘 구현
# 대소 비교, 위치 바꾸기
for n in range(N):
    my_list.append(int(input()))

for i in range(N):
    for j in range(i+1, N):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]

for n in range(N):
    print(my_list[n])



