# 프로그래머스 큰 수
# 질문게시판 보고 해답 보고 풀었음
# 처음에 permutation으로 완탐돌리려고 했는데, 시간초과 났음

def solution(numbers):
	numbers = list(map(str, numbers))
	answer = ''
	tuples = []
	for number in numbers:
		tmp = number
		while len(tmp) < 4:
			tmp = tmp * 2

		tuples.append((number, tmp[0:4]))

	tuples = sorted(tuples, key=lambda x: x[1])[::-1] # 두번째 요소를 기준으로 내림차순으로 정렬
	# print(tuples)
	for n, _ in tuples:
		answer += n

	return str(int(answer))

print(solution([3, 30, 34, 5, 9]))


# 또 다른 실패한 코드
'''
def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x: x[0])[::-1]
    answer = ''
    i = 0
    while i < len(numbers) - 1:
        for j in range(i+1, len(numbers)):
            if numbers[i][0] != numbers[j][0]:
                j -= 1
                break
        if i == j:
            answer += numbers[i]
            i += 1
            continue
        else:
            # print(numbers[i:j+1])
            MAX = len(str(max(map(int, numbers[i:j+1])))) # 최대 자릿수 찾기
            # print(MAX)
            tmp = []
            for k in range(i, j+1):
                tmp.append((numbers[k], numbers[k] + numbers[k][0] * (MAX - len(numbers[k]))))
            tmp.sort(key=lambda x: (int(x[1]), x[0]))
            tmp = tmp[::-1]
            # print(tmp)
            front = tmp[0][1]
            answer += tmp[0][0]
            for nums in tmp[1:]:
                if front == nums[1] and len(nums[0]) == 2 and len(set(nums[0])) == 2:
                    if nums[0][0] < nums[0][1]: # 뒷자리가 더 크면
                        answer = nums[0] + answer
                        continue

                answer += nums[0]

            i = j+1

    if i == len(numbers) - 1:
        answer += numbers[-1]

    return str(int(answer))
'''

