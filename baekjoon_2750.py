# 20220428
# 수 정렬하기
# https://www.acmicpc.net/problem/2750

cnt = int(input())

input_list = []
for i in range(cnt):
    input_list.append(int(input()))

# list.sort() 와 sorted(list)의 차이
# => 전자 .sort는 본체의 리스트를 정렬해서 변환
# => 후자 sorted는 본체 리스트는 그대로 두고, 정렬한 새로운 리스트를 반환
sorted_list = sorted(input_list)

for k in sorted_list:
    print(k)