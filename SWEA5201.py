# SWEA 5201 컨테이너 운반

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split())) # N개
    limits = list(map(int, input().split())) # M개
    lst = [0] * M # 트럭에 실은 화물 무게

    weights.sort(reverse=True)
    limits.sort(reverse=True)

    i = 0
    for w in weights:
        if w <= limits[i]:
            lst[i] = w
            i += 1
        if i == M:
            break

    result = sum(lst)
    print(f'#{test} {result}')


# 문제를 응용해보자..!
# 더 이상 들어갈 수 있는 곳이 없을때까지 넣기
# 일단 무거운거부터 채우고
# 가벼운 것도 lst[0]부터 채우기
# 화물을 다 싣거나, 실을 수 있는 화물차가 없는 경우 종료
# i = 0
# cnt = 0
# for w in weights:
#     while True:
#         if cnt == M: # M개 다 돌았는데 실을 수 있는 화물차가 없다 -> break
#             break
#         if lst[i] + w <= limits[i]:
#             lst[i] += w
#             cnt = 0
#             break
#         else:
#             i = (i+1) % M
#             cnt += 1
