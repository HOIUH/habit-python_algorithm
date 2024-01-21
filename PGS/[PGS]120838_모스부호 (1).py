# 240121
# [PGS] 모스부호 (1) / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120838

def solution(letter):
    morse = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z'}
    # 풀이 1
    # for문과 split 사용
    '''
    answer = ''
    letter = letter.split(" ")
    for e in letter:
        answer += morse[e]
    return answer
    '''

    # 풀이 2
    # string으로 합치는 역할인 join과 split 사용
    return ''.join(morse[e] for e in letter.split(" "))


