# SWEA 5247 연산

def calculate(c, number):
    if c == '+1':
        return number + 1
    elif c == '-1':
        return number - 1
    elif c == '*2':
        return number * 2
    elif c == '-10':
        return number - 10


T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())

    calc = ['+1', '-1', '*2', '-10']
    visited = [False] * 1000001
    results = [N]
    visited[N] = 1
    i = 0
    while True:
        n = results[i]

        if n == M:
            result = visited[n] - 1
            break

        for c in calc:
            new = calculate(c, n)
            if 0 < new <= 1000000 and not visited[new]:
                results.append(new)
                visited[new] = visited[n] + 1
        i += 1
    print(f'#{test} {result}')