# 221101
# JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951
'''
1. title(): 알파벳 외의 문자(숫자, 특수기호, 띄어쓰기 등)로 나눠져 있는 영단어들의 첫 글자를 모두 대문자로.  ex) 3People Unfollowed Me
cf) capitalize(): 맨 첫글자만 대문자로 변환. 단, 영문자일때만
2. 정규표현식에서 괄호는 그룹을 지정
'''

import re


def solution(s):
    s = s.title()

    # 정규표현식에서 괄호는 그룹을 지정
    # ([0-9]) => group(1) | ([A-Z]) => group(2)
    s = re.sub('([0-9])([A-Z])', lambda x: x.group(1) + x.group(2).lower(), s)
    return s


print(solution("3people unFollowed me"))
print(solution("for the last week"))
