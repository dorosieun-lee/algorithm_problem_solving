# 프로그래머스 JadenCase 문자열 만들기
# 공백 처리가 키포인트
def solution(s):
    IsSpace = [True if c.isspace() else False for c in s] # 공백인 위치 체크
    print(IsSpace)
    words = list(s.split()) # 단어 잘라서 리스트에 저장
    answer = ''
    idx = 0 # IsSpace를 훑는데 사용되는 인덱스
    w_idx = 0 # words를 훑는데 사용되는 인덱스
    while idx < len(s):
        if IsSpace[idx]: # 공백이 있던 자리면
            answer += ' ' # 공백을 하나 추가하고
            idx += 1 # 인덱스 추가
        else: # 단어가 있던 자리면
            word = words[w_idx]
            word = word[0].upper() + word[1:].lower() # 단어 앞자리만 대문자 처리해서
            answer += word # 추가
            idx += len(word) # 단어 길이만큼 idx 증가시킴
            w_idx += 1 # 단어 인덱스도 증가시킴

    return answer