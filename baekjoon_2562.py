# 20220412
# 최댓값
# https://www.acmicpc.net/problem/2562

'''
input = list(map(int, input().splitlines()))
max_value = max(input)
print(max_value)
print(input.index(max_value)+1)
'''

#input = list(input() for _ in range(9))
#채점결과 오답이라고 나옴


input_list = []

for i in range(9):
    input_list.append(int(input()))

max_value = max(input_list)
print(max_value)
print(input_list.index(max_value)+1)


