# 백준 10430번 문제
# 나머지

a, b, c = map(int, input().split())

if a < 2 or a > 10000 or b < 2 or b > 10000 or c < 2 or c > 10000:  # 이 부분을 깔끔하게 바꾸고 싶음
    print("input은 2 이상 10000 이하의 정수여야 합니다. 다시 입력하세요:")
    a, b, c = map(int, input().split())

print(a, b, c)

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
