# Baekjoon 2564 경비원
# 조건문이 너무 많다..
# 좀 더 깔끔하게 풀 수는 없을까..

width, height = map(int, input().split())
N_store = int(input())
stores = []
dist = 0
for _ in range(N_store):
    # 방향 : 1 = 북쪽, 2 = 남쪽, 3 = 서쪽, 4 = 동쪽
    # 거리 : 북,남쪽은 왼쪽 경계로부터의 거리, 동,서쪽은 위쪽 경계로부터의 거리
    stores.append(list(map(int, input().split()))) # 방향, 거리

Dongguen = list(map(int, input().split()))

if Dongguen[0] == 1:
    for store in stores:
        if store[0] == 1:
            dist += abs(Dongguen[1] - store[1])
        elif store[0] == 2:
            path1 = (width-Dongguen[1]) + height + (width-store[1])
            path2 = Dongguen[1] + height + store[1]
            dist += min(path1, path2)
        elif store[0] == 3:
            dist += Dongguen[1] + store[1]
        elif store[0] == 4:
            dist += (width - Dongguen[1]) + store[1]

if Dongguen[0] == 2:
    for store in stores:
        if store[0] == 2:
            dist += abs(Dongguen[1] - store[1])
        elif store[0] == 1:
            path1 = (width-Dongguen[1]) + height + (width-store[1])
            path2 = Dongguen[1] + height + store[1]
            dist += min(path1, path2)
        elif store[0] == 3:
            dist += Dongguen[1] + (height - store[1])
        elif store[0] == 4:
            dist += (width - Dongguen[1]) + (height - store[1])

if Dongguen[0] == 3:
    for store in stores:
        if store[0] == 3:
            dist += abs(Dongguen[1] - store[1])
        elif store[0] == 4:
            path1 = (height-Dongguen[1]) + width + (height-store[1])
            path2 = Dongguen[1] + width + store[1]
            dist += min(path1, path2)
        elif store[0] == 1:
            dist += Dongguen[1] + store[1]
        elif store[0] == 2:
            dist += (height - Dongguen[1]) + store[1]

if Dongguen[0] == 4:
    for store in stores:
        print(dist)
        if store[0] == 4:
            dist += abs(Dongguen[1] - store[1])
        elif store[0] == 3:
            path1 = (height-Dongguen[1]) + width + (height-store[1])
            path2 = Dongguen[1] + width + store[1]
            dist += min(path1, path2)
        elif store[0] == 1:
            dist += Dongguen[1] + (width - store[1])
        elif store[0] == 2:
            dist += (height - Dongguen[1]) + (width - store[1])

print(dist)