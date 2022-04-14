# 20220414
# 나머지
# https://www.acmicpc.net/problem/3052

l = []

for i in range(10):
    l.append(int(input()) % 42)

# list 속 중복값을 제거하기 위해 집합으로 형변환
set_l = set(l)

#print(set_l)

print(len(set_l))

