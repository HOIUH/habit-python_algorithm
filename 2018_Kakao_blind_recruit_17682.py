# 221117
# 2018 KAKAO BLIND RECRUITMENT > [1차] 다트 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17682
import re


def solution(dartResult):
    answer = 0
    tmp = []
    bonuses = ['S', 'D', 'T']

    # 정규표현식 ?의 의미: 앞 패턴이 있어도 되고 없어도 되고.
    result = re.match('([0-9]{1,2}[A-Z][#*]?)([0-9]{1,2}[A-Z][#*]?)([0-9]{1,2}[A-Z][#*]?)', dartResult)

    for element in result.groups():
        e = re.match('([0-9]{1,2})([A-Z])([#*])?', element)
        score, bonus, option = int(e.group(1)), e.group(2), e.group(3)
        score = score ** (bonuses.index(bonus) + 1)

        if option == '*':
            if tmp:
                tmp[-1] = tmp[-1]*2
            score = score * 2
        elif option == '#':
            score = score * (-1)
        tmp.append(score)

    for t in tmp:
        answer += t

    return answer


print(solution('1D2S#10S'))
print(solution('1D2S0T'))
