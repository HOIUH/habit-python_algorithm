# 20220425
# 단어 공부
# https://www.acmicpc.net/problem/1157

words = input().upper()
unique_words = list(set(words)) # 입력받은 문자열에서 중복값 제거

cnt_list = []
for x in unique_words:
    cnt = words.count(x)    # 입력받은 문자열에서 특정 문자 count값 구함
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])

'''
s = input().upper()

d = dict()
for i in range(len(s)):
    k = s[i]

    if k in d:
        now_val = d[k]
        d[k] = now_val + 1
    else:
        d[k] = 1

max_val = max(d.values())

result = []
for key in d:
    if d[key] == max_val:
        result.append(key)

if len(result) == 1:
    print(result[0])
else:
    print('?')
'''
