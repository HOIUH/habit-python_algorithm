# 221103
# 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    b = bin(n)  # 리턴 타입 str
    b = b.count('1')

    while True:
        n += 1
        if bin(n).count('1') == b:
            return n

print(solution(78))