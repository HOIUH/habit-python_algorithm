# 221110
# 핸드폰 번호 가리기
# https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    l = len(phone_number)
    phone_number = '*' * (l-4) + phone_number[l-4:]
    return phone_number

print(solution("01033334444"))
