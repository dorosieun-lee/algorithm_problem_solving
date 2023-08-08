# 떡볶이 떡 만들기
# 문제:
# 오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다.
# 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.
# 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
# 예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를
# 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다
# 절단 떡의 길이는 차례대로 4, 0, 0, 2cm이다. 손님은 6cm만큼의 길이를 가져간다.
# 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해
# 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

# input data
# 4 6
# 19 15 10 17

import time

N, M = [4, 6] #map(int, input().split()) # N: 떡의 개수, M: 요청한 떡의 길이
height = [19, 15, 10, 17] #list(map(int, input().split())) # 떡의 개별 높이 (각 높이는 0보다 크고 10억보다 작거나 같다)

start = time.time()
# 이진 탐색 사용 X
for h in range(max(height), 0, -1):
    get = 0
    for dduck in height:
        if dduck - h > 0:
            get += dduck - h

    if get >= M:
        break

print(h)
print(f"time : {time.time() - start: 0.10f}") # 0.0010023117


start = time.time()
# 이진 탐색 사용 O
# 이진 탐색의 개념인 중간값을 이용
height = sorted(height)
if len(height) % 2 == 0: # 떡의 개수가 짝수이면
    h = (height[len(height)//2 - 1] + height[len(height)//2]) // 2

else:
    h = height[len(height)//2]

while True:
    get = 0
    for dduck in height:
        if dduck - h > 0:
            get += dduck - h

    if get > M:
        h += 1
        continue
    elif get < M:
        h -= 1
        continue
    elif get == M:
        break

print(h)
print(f"time : {time.time() - start: 0.10f}") # 0.0000000000