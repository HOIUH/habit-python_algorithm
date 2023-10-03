# 231003
# [PGS] 영어가 싫어요 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120894

def solution(numbers):
    # 나의 풀이
    # 리스트와 인덱스 사용
    '''
    numbers_en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(numbers_en)):
        numbers = numbers.replace(numbers_en[i], str(i))

    return int(numbers)
    '''

    # 다른 사람 풀이
    # enumerate 사용 => List의 index와 value를 unpacking
    for num, en in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(en, str(num))
    return int(numbers)


print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixseven"))
