# 20220413
# 숫자의 개수
# https://www.acmicpc.net/problem/2577

input_list = []

for i in range(3):
    input_list.append(int(input()))

m = input_list[0] * input_list[1] * input_list[2]

str_m = str(m)
#print('str_m: ', str_m)

result_list = [0]*10

for i in str_m:
    result_list[int(i)] += 1

for i in result_list:
    print(i)

'''
r0 = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
r7 = 0
r8 = 0
r9 = 0

for k in range(0, len(str_m)):
    if str_m[k] == '0':
        r0 += 1
    elif str_m[k] == '1':
        r1 += 1
    elif str_m[k] == '2':
        r2 += 1
    elif str_m[k] == '3':
        r3 += 1
    elif str_m[k] == '4':
        r4 += 1
    elif str_m[k] == '5':
        r5 += 1
    elif str_m[k] == '6':
        r6 += 1
    elif str_m[k] == '7':
        r7 += 1
    elif str_m[k] == '8':
        r8 += 1
    elif str_m[k] == '9':
        r9 += 1

print(r0)
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)
print(r7)
print(r8)
print(r9)

'''






