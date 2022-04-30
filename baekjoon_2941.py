# 20220430
# 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

# dz=는 z= 보다 앞 순서에 배치되어야 함
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str_i = input()

# 다른 사람 풀이
# 크로아티아 알파벳 종류별 개수가 아닌 전체 개수니까
# 전체 치환하면 됨
for i in croatia:
    str_i = str_i.replace(i, '^')

print(len(str_i))

# 내 풀이
'''
cnt = 0
for i in croatia:

    # i가 처음 등장하는 위치 찾음
    find_index = str_i.find(i)

    while find_index != -1:
        cnt += 1
        str_i = str_i.replace(i, '^', 1)    # 이번에 찾은 i에 대해서만 ^로 치환
        find_index = str_i.find(i)

# ^ 제외한 문자들은 크로아티아 알파벳 아닌 보통 알파벳벳
aftr_replace = len(str_i.replace('^', ''))
print(cnt+after_replace)
'''

'''
find_idx = str_i.find('dz=')
print(find_idx)
print(find_idx+len('dz='))
print(str_i.replace('dz=', ','))
'''