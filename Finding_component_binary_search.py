# 부품찾기
# 문제:
# 동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
# 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
# 동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개의 종류를 모두 확인해서 견적서를 작성해야 한다.
# 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자

N = int(input()) # 첫째 줄은 정수 N, 가게에서 가지고 있는 부품의 갯수
have = list(map(int, input().split())) # 두번째 줄은 가게에서 가지고 있는 부품의 목록
M = int(input()) # 세번째 줄은 손님이 요청한 물건의 갯수
want = list(map(int, input().split())) # 네번째 줄은 손님이 요청한 물건의 목록

# 이진탐색 사용 X
ans = []
for m in range(M):
    if want[m] in have:
        ans.append('yes')
    else:
        ans.append('no')

print(*ans)


# 이진 탐색 사용 O
ans = []


def binary_search(start, end, arr, key):
    if start > end:
        return "no"

    mid = (start+end) // 2
    if arr[mid] == key:
        return "yes"
    elif arr[mid] < key:
        return binary_search(mid+1, end, arr, key)
    elif arr[mid] > key:
        return binary_search(start, mid-1, arr, key)


for m in range(M):
    ans.append(binary_search(0, len(have), sorted(have), want[m]))


print(*ans)