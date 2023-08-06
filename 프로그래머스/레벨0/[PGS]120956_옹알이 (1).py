# 230806
# [PGS] 옹알이 (1) / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    # 나의 풀이
    # 각 babbling 요소마다 앞에서부터 문자열 비교한 후 slicing하여 다시 비교
    '''
    answer = 0
    l = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        while b:
            if b[:2] in l:
                b = b[2:]
            elif b[:3] in l:
                b = b[3:]
            else:
                break

            if not b:
                answer += 1

    return answer
    '''

    # 다른 사람 풀이
    # 정규표현식 활용
    # re.compile은 정규식 객체 반환. 재사용 가능하도록.
    # 참고: https://namhandong.tistory.com/65
    import re

    answer = 0
    regex = re.compile('^(aya|ye|woo|ma)+$')
    # ^ : 이 패턴으로 시작해야함
    # $ : 이 패턴으로 종료해야함
    # | : 두 패턴 중 하나여야 함 (OR 기능)
    # + : 앞 패턴이 하나 이상이어야 함

    for b in babbling:
        if regex.match(b):
            answer += 1

    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
