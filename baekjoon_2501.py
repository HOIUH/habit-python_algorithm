# 20220421
# 약수 구하기
# https://www.acmicpc.net/problem/2501

input_list = list(map(int, input().split()))

num = input_list[0]
order = input_list[1]
measure_list = []

for i in range(1, num+1):
    if num % i == 0:
        measure_list.append(i)
#print(measure_list)

if len(measure_list) < order:
    print('0')
else:
    print(measure_list[order-1])

