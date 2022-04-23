# 20220423
# 알파벳 찾기
# https://www.acmicpc.net/problem/10809

s = input().lower()
abc = 'abcdefghijklmnopqrstuvwxyz'

#l = [-1] * 26

for i in abc:   # 처음 등장하는 위치 구하기 위해 abc로 for문 돌림
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')

