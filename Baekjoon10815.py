# Baekjoon 10815 숫자 카드

def binary_search(start, end, array, key):
    mid = (start + end) // 2
    if start > end:
        return 0
    if array[mid] == key:
        return 1
    elif array[mid] < key:
        return binary_search(mid+1, end, array, key)
    else:
        return binary_search(start, mid-1, array, key)


N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

cards.sort() # 오름차순 정렬

result = []
for n in nums:
    is_exist = binary_search(0, len(cards)-1, cards, n)
    result.append(is_exist)

print(*result)

