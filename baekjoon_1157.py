# 20220425
# 단어 공부
# https://www.acmicpc.net/problem/1157

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
