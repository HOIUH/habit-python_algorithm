# 20220429
# A+B - 7
# https://www.acmicpc.net/problem/11021

t = int(input())

total_list = []

for i in range(t):
    input_list = list(map(int, input().split()))
    #a, b = map(int, input().split())
    total_list.append(input_list)

for i in range(t):
    sum = total_list[i][0]+total_list[i][1]
    print(f'Case #{i+1}: {sum}')

    # 아래 출력 결과는 Case # 1 :  2 => 의도치 않은 스페이스가 생김
    #print('Case #', i+1, ': ', total_list[i][0]+total_list[i][1])

