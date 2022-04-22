# 20220422
# 이진수
# https://www.acmicpc.net/problem/3460

test_cnt = int(input())

input_list = list(map(int, input().split()))

for i in range(test_cnt):

    # 결과: 0b1101
    # <class 'str'>
    #b = bin(input_list[i])  # 10진수를 2진수로 변환

    b = format(input_list[i], 'b')

    result = []
    for k in range(len(b)-1, -1, -1):
        if b[k] == '1':
            result.append((len(b)-1) - k)

    print(*result)




