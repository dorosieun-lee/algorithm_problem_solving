# def solution(people, limit):
#     result = 0
#     on_boat = []
#
#     people.sort()  # 내림차순 정렬
#
#     for i in range(len(people) - 1, -1, -1): # 여기를 손대서 반복 횟수를 줄일 수 있을 것 같음
#         for j in range(0, i):
#             if people[i] + people[j] <= limit and i not in on_boat and j not in on_boat:
#                 result += 1
#                 on_boat.extend([i, j])
#             else:
#                 continue
#
#     result += len(people) - len(on_boat)
#
#     return result
#
# people = [70, 60, 50]
# limit = 100
# print(solution(people, limit))

# 시간 초과!!

def solution(people, limit):
    people.sort()
    boat = 0
    start = 0
    end = len(people)-1
    while True:
        if start > end:
            break
        elif start == end:
            boat += 1
            break

        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
            boat += 1
        else:
            end -= 1
            boat += 1
    return boat

people = [70, 80, 50]
limit = 100
print(solution(people, limit))
