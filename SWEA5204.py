# SWEA 5204 병합 정렬

def merge_sort(lst):
    if len(lst) == 1: return lst

    mid = len(lst) // 2
    left = lst[0:mid]
    right = lst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    my_lst = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            my_lst.append(left[i])
            i += 1
        else:
            my_lst.append(right[j])
            j += 1

    if i < len(left):
        while i < len(left):
            my_lst.append(left[i])
            i += 1
    elif j < len(right):
        while j < len(right):
            my_lst.append(right[j])
            j += 1
    return my_lst


T = int(input())

for test in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    numbers = merge_sort(numbers)

    print(f'#{test} {numbers[N//2]} {cnt}')
