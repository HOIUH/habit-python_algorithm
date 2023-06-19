# 230619
# [PGS] 겹치는 선분의 길이 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120876

# 모든 선분의 겹치는 부분을 중복없이 구해야하므로 교집합, 합집합 활용
def solution(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))

    return len(s1 & s2 | s2 & s3 | s3 & s1)
