# 20220503
# A+B - 4
# https://www.acmicpc.net/problem/10951

import sys

while True:
    # 예외처리 하지 않으면 런타임에러(ValueError 발생)
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break

# 참고
# [Python 문법] 파이썬 입력 받기 (sys.stdin.readline)
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline




