# 220724
# 2020 KAKAO BLIND RECRUITMENT > 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

# 참고: https://pearlluck.tistory.com/589

def solution(s):
    answer = len(s)

    if len(s) == 1:
        return 1

    for k in range(1, len(s)//2+1): # 문자열 절반까지만 확인
        x = ''
        cnt = 1
        tmp = s[:k] # 단위문자열 초기화

        for i in range(k, len(s)+k, k):
            if tmp == s[i:i+k]: # 문자열 슬라이싱은 length 넘어가도 에러나지 않음
                cnt += 1
            else:
                if cnt == 1:
                    x += tmp
                else:
                    x += str(cnt) + tmp
                tmp = s[i:i+k]  # 단위문자열 변경
                cnt = 1

        answer = min(answer, len(x))

    return answer

# s = "aabbaccc"
# print(solution(s))
# print(f'|a{s[8:12]}a|')

'''
# 다른 사람 풀이 참고하기
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))
'''

'''
# 나의 풀이
# 오답
def solution(s):
    answer = []
    
    for k in range(1, len(s)+1):    # 문자열 자르는 단위 1부터 len(s)까지
        x = ''
        cnt = 1
        if len(s) % k == 0:
            for i in range(0, len(s), k):
                if i != len(s)-k:   # IndexError 방지위함
                    if s[i:i+k] == s[i+k:(i+k*2)]:
                        cnt += 1                        
                    else:
                        if cnt > 1:
                            x = x + str(cnt) + s[i:i+k]
                            cnt = 1
        answer.append(len(x))
        
    return min(answer)
'''