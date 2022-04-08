
a, b, c = map(int, input().split())
# a 고정비용, b 가변비용, c 판매비용
# c * quantity > a+b*quantity
#c*q-b*q > a
#(c-b)*q > a
#q > a/(c-b)

# quantity 판매량

if c <= b:
    print('-1')
else:
    '''
    quantity = 1
    while quantity <= a/(c-b):
        quantity += 1
    print(quantity)
    '''
    print(a//(c-b)+1)







