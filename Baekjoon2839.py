# Baekjoon 2839 설탕배달

N = int(input())

A = N//5 + 1
B = N//3 + 1
able = []

for a in range(A):
    for b in range(B):
        SUM = 5*a + 3*b
        if SUM == N:
            able.append(a+b)

if len(able) == 0:
    result = -1
else:
    result = min(able)

print(result)