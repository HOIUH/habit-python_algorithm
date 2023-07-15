# 230716
# [PGS] 이진수 더하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120885

# bin(): 10진수를 2진수로 변환. 예) bin(9) => '0b1001'
# int(): 10진수로 변환. 예) int('0b1001', 2) => 9

def solution(bin1, bin2):

    bin1 = int('0b'+bin1, 2)
    bin2 = int('0b'+bin2, 2)

    return bin(bin1+bin2)[2:]

