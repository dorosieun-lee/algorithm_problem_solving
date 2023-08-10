# SWEA2005 파스칼의 삼각형

T = int(input())

for test in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)] # NxN array 생성

    for i in range(N):
        for j in range(0, i+1):
            if j in [0, i]:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{test}')
    for i in range(N):
        print(*arr[i][:i+1])

"""
강사님 코드
0번째 열, 0번째 행을 추가해서 arr[1][1] = 1 만 초기값으로 두고
그 뒤는 반복문 돌려서 풀 수도 있음
"""

