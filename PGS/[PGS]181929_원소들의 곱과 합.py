# 240331
# [PGS] 원소들의 곱과 합 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/181929

def solution(num_list):
    gob = 1
    for num in num_list:
        gob *= num
    hab = sum(num_list) ** 2

    return 1 if gob < hab else 0
