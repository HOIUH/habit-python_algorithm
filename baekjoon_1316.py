# 20220507
# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

import sys

cnt = int(input())

# strip() : 문자열 맨 앞과 맨 끝의 공백문자 제거
input_list = [sys.stdin.readline().strip() for i in range(cnt)]

result = cnt
for word in input_list:
    for i in range(len(word)-1):    # 마지막 문자는 확인할 필요 없음

        if word[i] == word[i+1]: continue   # 여기서는 continue 대신 pass 써도 상관없음
        elif word.find(word[i], i+1) > -1:
            result -= 1
            break

print(result)

'''
word[i]
    input_list[i]
    input_list.replace()
    
input_list = []
for _ in range(cnt):
    word = sys.stdin.readline().split()
    input_list.append(word)
    
# 결과: [['happy'], ['new'], ['year']]
print(input_list)
'''