# Baekjoon 2212 센서

# 고속도로에 N개의 센서를 설치
# 최대 K개의 집중국을 세울 수 있음
# 각 집중국 수신 가능 영역의 길이의 합을 최소화해야 함
# 고속도로는 평면상의 직선이라고 가정
# 센서의 좌표가 같을 수도 있다

N = int(input())
K = int(input())
# 중복 제거 및 정렬
sensors = list(set(map(int, input().split())))
sensors.sort()
len_s = len(sensors)
print(sensors)
dist = sensors[-1] - sensors[0]
# print(dist)
MAX = dist // K
i = 0

lst = []
while len(lst) < K:
    j = i
    while True:
        j += 1
        # lst가 K개만큼 안되었는데, j 가 끝이 되어버리면 MAX를 하나 줄이고 다시 처음부터 해보기

        if sensors[j] - sensors[i] > MAX:
            print(i, j)
            lst.append((sensors[i], sensors[j-1]))
            i = j
            break
# print(lst)
total = 0
for l in lst:
    total += l[1] - l[0]

print(total)

6
2
1 6 9 3 6 7

1 3 6 7 9 -> 4




