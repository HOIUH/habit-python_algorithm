# 231003
# [PGS] 인덱스 바꾸기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120895

def solution(my_string, num1, num2):
    # 나의 풀이
    # 문자열 슬라이싱과 재배치 활용
    '''
    mn, mx = min(num1, num2), max(num1, num2)
    ch1, ch2 = my_string[mn], my_string[mx]
    answer = my_string[:mn] + ch2 + my_string[mn+1:mx] + ch1 + my_string[mx+1:]

    return answer
    '''

    # 다른 사람 풀이 1
    # 문자열 슬라이싱과 재배치 활용
    # min, max 함수 대신 sorted 사용
    '''
    [mn, mx] = sorted([num1, num2])     # mn, mx를 변수로 사용할 수 있음
    ch1, ch2 = my_string[mn], my_string[mx]
    answer = my_string[:mn] + ch2 + my_string[mn + 1:mx] + ch1 + my_string[mx + 1:]

    return answer
    '''

    # 다른 사람 풀이 2
    # string에서 list로 형 변환 후 요소 재배치 후, join
    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]
    return ''.join(s)


print(solution("hello", 1, 2))
