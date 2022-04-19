# 20220419
# 아스키 코드
# https://www.acmicpc.net/problem/11654

i = input() # 0 입력해도 str으로 인식

#print(type(i))

if type(i) is str:  # 입력값의 타입이 문자형인 경우
    print(ord(i))   # 문자형의 아스키 코드값은 ord로 구함
else:
    print(chr(i))   # 아스키 코드값에 해당하는 문자는 chr로 구함