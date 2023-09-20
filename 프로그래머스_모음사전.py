# 프로그래머스 모음사전

def make_word(char):
    global words
    words.append(char)
    vowels = 'AEIOU'
    if len(char) == 5:
        return

    for v in vowels:
        make_word(char+v)

words = []
make_word('')

def solution(word):
    global words
    answer = words.index(word)
    return answer

print(solution('AAAAE'))