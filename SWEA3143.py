# SWEA 3143 가장 빠른 문자열 타이핑
# 슬라이싱, 내장함수 사용 X 하려 했으나 슬라이싱해버림~

"""
런타임 에러남 -> 이유: 만약 strA = aaabababa 이고 strB = aa인 경우,
실제로는 aa를 한번만 쓸 수 있지만
코드 상에서는 i를 하나씩 증가하며 검사하기 때문에
[0:2], [1:3] 이렇게 중복되서 aa를 사용하는걸로 계산하게 된다.
따라서 i를 1씩 증가시키는게 아니라, 한번 strB를 사용했으면 그 뒤부터 탐색해주는 식으로 해야함

T = int(input())

for test in range(1, T+1):
    strA, strB = input().split()
    cnt = 0

    for i in range(len(strA)-len(strB)+1):
        for j in range(len(strB)):
            if strA[i+j] != strB[j]:
                break
        else:
            cnt += 1

    cnt = len(strA) - cnt * len(strB) + cnt

    print(f'#{test} {cnt}')
"""


T = int(input())
for test in range(1, T+1):
    strA, strB = input().split()
    cnt = 0
    i = 0

    while i < len(strA) - len(strB) + 1:
        if strA[i:i+len(strB)] == strB:
            cnt += 1
            i += len(strB)
        else:
            i += 1

    cnt = len(strA) - cnt * len(strB) + cnt

    print(f'#{test}', cnt)


