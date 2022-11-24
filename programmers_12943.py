# 221124
# 콜라츠 추측
# https://school.programmers.co.kr/learn/courses/30/lessons/12943

def Collatz(n, output):
    if n == 1:
        return output
    elif output == 500:
        return -1

    remainder = n % 2
    if remainder:  # 홀수인 경우
        n = n * 3 + 1
    else:  # 짝수인 경우
        n = n / 2

    output += 1
    return Collatz(n, output)   # return 없이 재귀 돌리면 None 반환


def solution(num):
    return Collatz(num, 0)


print(solution(6))
