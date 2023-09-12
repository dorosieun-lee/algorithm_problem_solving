def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for row in range(len(arr1)):
        for col in range(len(arr2[0])):
            num = 0
            for i in range(len(arr1[0])):
                num += arr1[row][i] * arr2[i][col]
            answer[row][col] = num
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3, 2], [3, 3, 2]]

print(solution(arr1, arr2))