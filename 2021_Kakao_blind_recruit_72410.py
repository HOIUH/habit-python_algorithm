# 221011
# 2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천
# https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)

    # 3단계
    # . 메타 문자는 줄바꿈 문자인 \n 을 제외한 모든 문자와 매치됨 => 일반 문자로 사용하려면 \.로 표기
    # .이 1번 이상 반복되면 . 으로 치환
    newid = re.sub('\.+', '.', new_id)

    # 4단계
    new_id = re.sub('(^\.)|(\.$)', '', new_id)
    # new_id = re.sub('^[.]|[.]$', '', new_id)

    # 5단계
    new_id = 'a' if new_id == '' else new_id
    # if new_id == '': new_id = 'a'

    # 6단계
    new_id = re.sub('(\.$)', '', new_id[:15])

    # 7단계
    if len(new_id) <= 2:
        new_id += new_id[-1] * 2
        new_id = new_id[:3]

    return new_id


# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
print(solution("z-+.^."))
