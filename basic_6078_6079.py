# basic_6078
'''
i = ''

while i != 'q':
    print('input을 입력하세요: ')
    i = input()
'''

# basic_6079
print('input을 입력하세요: ')
i = int(input())

total = 0

for j in range(0, i-1):
    if total <= i:
        total += j
        print(total)
    else: break

print('total: ', total)



