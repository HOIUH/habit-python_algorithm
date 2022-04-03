import re

input1 = "A man, a plan, a canal: Panama"
input2 = "race a car"

# 데크 자료형을 이용한 자료화
def isPalindrome_slicing(s: str) -> bool:

    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    print(s)
    print(s[::-1])

    return s == s[::-1] # 슬라이싱

print(isPalindrome_slicing(input1))
print(isPalindrome_slicing(input2))



