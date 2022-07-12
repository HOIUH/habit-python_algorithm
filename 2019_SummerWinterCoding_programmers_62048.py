# 220712
# 멀쩡한 사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/62048

# 전체사각형개수 - 빼야하는 사각형 개수 * 최대공약수

from math import gcd

# 나의 풀이에서 필요 없는 부분 덜어낸 코드
# min, max 값 구할 필요 없음
def solution(w,h):
    answer = 1
    gcd_num = gcd(w, h)
    divided_w = w // gcd_num
    divided_h = h // gcd_num
    answer = w * h - (divided_w + divided_h - 1) * gcd_num

    return answer

# 나의 풀이
'''
def solution(w,h):
    answer = 1
    gcd_num = gcd(w, h)
    divided_w = w // gcd_num
    divided_h = h // gcd_num
    max_num = max(divided_w, divided_h)
    min_num = min(divided_w, divided_h)
    answer = w * h - (max_num + min_num - 1) * gcd_num
    
    return answer
'''

# math 라이브러리 못 사용하는 경우
'''
def gcd(x, y):
   # y가 0이 될 때까지 반복
   while y:
       # y를 x에 대입
       # x를 y로 나눈 나머지를 y에 대입
       x, y = y, x % y
   return x
'''