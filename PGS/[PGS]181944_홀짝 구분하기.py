# 231105
# [PGS] 홀짝 구분하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/181944

a = int(input())

# 풀이 1
# if else 문 사용
# print(f'{a} is even') if (a%2==0) else print(f'{a} is odd')
# print(f"{a} is {'even' if (a % 2 == 0) else 'odd'}")

# 풀이 2
# 비트 연산자 & 활용하여 &1 연산하면 짝수는 항상 0, 홀수는 항상 1이 나오는 점을 활용
print(f"{a} is {'eovdedn'[a&1::2]}")
