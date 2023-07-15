# 230716
# [PGS] A로 B 만들기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120886

# 문자열에는 sort() 함수 사용 불가
# (참고) 문자열 뒤집기: 슬라이싱 / reversed() 함수 사용 / list로 변환하고 list.reverse() 사용
# str[::-1] / ''.join(reversed(str)) / ''.join(list(str).reverse())

def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0
