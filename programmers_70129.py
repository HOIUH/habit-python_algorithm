# 220923
# 월간 코드 챌린지 시즌1 > 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

'''
1. bin(10진수 숫자) => 리턴값: str 형식. 0b1111 이런식으로 리턴됨
2. 변수 a, 변수 b 를 list에 넣어서 리턴하고 싶은 경우: [a, b]
'''

def solution(s):
    # 나의 풀이를 더 깔끔하게 만든 코드
    binary_conversion, deleted_zero = 0, 0

    while s != '1':
        len_before = len(s)
        s = s.replace('0', '')
        len_after = len(s)
        deleted_zero += len_before - len_after

        s = bin(len_after)[2:]=
        binary_conversion += 1

    return [binary_conversion, deleted_zero]

    # 나의 풀이
'''
    answer = []
    binary_conversion = 0
    deleted_zero = 0

    while s != '1':
        len_before = len(s)
        s = s.replace('0', '')
        len_after = len(s)
        deleted_zero += len_before - len_after

        # s = bin(len_after).replace('0b', '')
        s = bin(len_after)[2:]
        binary_conversion += 1

    answer.append(binary_conversion)
    answer.append(deleted_zero)

    return answer
'''

x = "110010101001"
print(solution(x))