# Baekjoon 1244 스위치 켜고 끄기

# 스위치는 1, 0으로 켜져 있음, 꺼져 있음을 나타내고 있음
# 학생들은 자연수를 부여받음
# 남학생: 스위치 번호가 자기가 받은 수의 배수이면, 스위치 상태를 바꾼다
# 여학생: 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를
# 포함하는 구간을 찾아서 스위치 상태를 모두 바꾼다. 스위치 개수는 항상 홀수

sw_N = int(input()) # 스위치 개수
switches = list(map(int, input().split()))

stu_N = int(input()) # 학생 수
for _ in range(stu_N):
    gender, num = map(int, input().split())
    if gender == 1: # 남학생이면
        idx = list(range(num, sw_N+1, num)) # 배수 리스트 -> +1 해주는거 중요! num==sw_N이면 빈 리스트가 됨
        for i in idx:
            switches[i-1] = 0 if switches[i-1] == 1 else 1 # 인덱스로 쓸거니까 i-1 해줌

    else: # 여학생이면
        mid = num-1
        start, end = mid, mid
        while True:
            start -= 1
            end += 1
            if start < 0 or end > sw_N-1: # 경계를 벗어나면
                start += 1
                end -= 1
                break
            if switches[start] != switches[end]:
                start += 1
                end -= 1
                break

        for i in range(start, end+1):
            switches[i] = 0 if switches[i] == 1 else 1  # 이미 앞에서 start, end는 인덱스로 구했으니까 i-1 할 필요 없음

for i, s in enumerate(switches):
    if i % 20 == 0 and i != 0:
        print('\n', end='')
    print(s, end=' ')

