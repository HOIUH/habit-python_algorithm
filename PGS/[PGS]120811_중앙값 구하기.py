# 240218
# [PGS] 중앙값 구하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120811

def solution(array):
    # 풀이 1
    # 리턴값 있는 sorted() 사용
    return sorted(array)[len(array)//2]

    # 풀이 2
    # 리턴값 없는 sort() 사용
    # array.sort()
    # return array[len(array)//2]

