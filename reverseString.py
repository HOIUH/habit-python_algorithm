input1 = ["h", "e", "l", "l", "o"]
input2 = ["H", "a", "n", "n", "a", "h"]

input3 = input1

def reverseString(l: list) -> list:
    result = []

    while len(l) > 0:
        result.append(l.pop())

    return result

# 리턴 없이 리스트 내부를 직접 조작하라
# 투 포인터를 이용한 스왑
def reverseString_noReturn(l: list) -> None:
    left, right = 0, len(l)-1

    while left < right:
        l[left], l[right] = l[right], l[left]

        left += 1   # 파이썬은 ++ 기능 지원하지 않음
        right -= 1

    print(l)

# 리턴 없이 리스트 내부를 직접 조작하라
# 파이썬다운 방식
def reverseString_python(l: list) -> None:  # list[str] 사용 시, TypeError: 'type' object is not subscriptable 에러 발생
    l.reverse() # reverse는 리스트에만 제공됨

    #l = l[::-1]    # 문자열 뒤집기 안 됨
    #l[:] = l[::-1]

    print(l)


#print(reverseString(input1))   # reverseString 함수에서 pop 사용해서 input1 내용 사라짐
#print(reverseString(input2))

'''
reverseString_noReturn(input3)
#reverseString_noReturn(input2)
print("input3: ", input3)
print("input1: ", input1)
'''

reverseString_python(input3)
reverseString_python(input2)
print("input3: ", input3)
print("input1: ", input1)








