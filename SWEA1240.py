# SWEA 1240 단순 2진 암호코드

# 2차원 배열 입력받아서
# 암호코드가 있는 부분 인덱스를 찾고 <- 암호코드의 끝은 항상 1로 끝난다
# 암호코드를 십진수로 변경하고 (주어진 코드 이용, 7개씩 자름)
# 암호코드가 규칙에 맞는지 확인하고 (홀수자리 합 * 3) + (짝수자리 합) = 10의 배수 (암호코드는 8자리)
# 맞으면 자리수의 합 반환, 틀리면 0 반환

my_dic = {'3211': 0, '2221': 1, '2122': 2, '1411': 3, '1132': 4,
          '1231': 5, '1114': 6, '1312': 7, '1213': 8, '3112': 9}
def bit_to_num(lst):
    before = 0
    cnt = 0
    tmp = ''
    for l in lst:
        if before == l:
            cnt += 1
            continue
        else:
            before = l
            tmp += str(cnt)
            cnt = 1
    tmp += str(cnt)
    return my_dic[tmp]

def num_check(numbers):
    odd = [] # 홀수번째 자리수 저장
    even = [] # 짝수번재 자리수 저장
    for i in range(0, 8, 2):
        odd.append(numbers[i]) # 0, 2, 4, 6
        even.append(numbers[i+1]) # 1, 3, 5, 7
    if (sum(odd) * 3 + sum(even)) % 10 == 0:
        return True
    else:
        return False


T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    #print(arr)
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == 1:
                break
        if arr[i][j] == 1:
            break

    code = arr[i][j-56+1:j+1]
    num_code = []
    for k in range(0, 56, 7):
        cut = code[k:k+7]
        #print(cut)
        num_code.append(bit_to_num(cut))

    if num_check(num_code):
        result = sum(num_code)
    else:
        result = 0

    print(f'#{test} {result}')

