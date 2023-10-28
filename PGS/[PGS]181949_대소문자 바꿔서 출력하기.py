# 231029
# [PGS] 대소문자 바꿔서 출력하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/181949

str = input().strip()
result = ''

for e in str:
    if e == e.lower():
        result += e.upper()
    else:
        result += e.lower()

print(result)
