# 20220424
# 문자열 반복
# https://www.acmicpc.net/problem/2675

t = int(input())

input_list = []
for i in range(t):
    l = list(input().split())
    input_list.append(l)
    #print(input_list)

for i in input_list:
    result = ''

    for k in i[1]:
        result = result + k*int(i[0])

    print(result)

