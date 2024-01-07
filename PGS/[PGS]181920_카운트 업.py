# 240107
# [PGS] 카운트 업 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/181920

def solution(start_num, end_num):
    # 풀이 1
    # for문과 list comprehension
    #return [i for i in range(start_num, end_num+1)]

    # 풀이 2
    # range 함수 사용
    return list(range(start_num, end_num+1))

print(solution(3, 10))

print(range(3, 10+1))   # 결과: range(3, 11)