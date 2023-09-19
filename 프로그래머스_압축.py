# 프로그래머스 압축

def solution(msg):
    answer = []
    my_dict = {'Z': 26}
    i = 0
    while i < len(msg):
        for j in range(len(msg), i-1, -1):
            word = msg[i:j]
            if word in my_dict.keys():
                answer.append(my_dict[word])
                if j < len(msg)-1:
                    my_dict[word+msg[j]] = max(my_dict.values()) + 1
                i = j
                break
        else:
            answer.append(ord(msg[i].upper()) - 64)
            if i < len(msg)-1:
                my_dict[msg[i:i+2]] = max(my_dict.values()) + 1
            i += 1

    #print(my_dict)
    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))