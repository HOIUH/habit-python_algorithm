# 20220420
# 숫자의 합
# https://www.acmicpc.net/problem/11720

cnt = int(input())

num = input()   # <class 'str'>

# split 메소드의 구분자를 지정하기 어려운 경우
# str형을 한글자씩 리스트로 저장하고 싶은 경우
num_list = list(num)
#num_list = num.split('', maxsplit=cnt)     # ValueError: empty separator 발생
#print(num_list)

sum_list = 0
for i in range(cnt):
    sum_list += int(num_list[i])

print(sum_list)




