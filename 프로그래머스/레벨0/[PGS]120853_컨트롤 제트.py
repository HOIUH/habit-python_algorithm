# 230703
# [PGS] 컨트롤 제트 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    answer, prev_val = 0, 0
    s = s.split()

    for e in s:
        if e == 'Z':
            answer -= prev_val
        else:
            answer += int(e)
            prev_val = int(e)

    return answer
