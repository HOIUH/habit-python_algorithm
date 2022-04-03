import collections

input1 = "A man, a plan, a canal: Panama"
input2 = "race a car"

# 데크 자료형을 이용한 최적화
def isPalindrome_deque(s: str) -> bool:

    # 자료형 데크로 선언
    #strs: Deque = collections.deque()
    strs = collections.deque()

    for char in s:
        if char.isalnum():  # 영문자, 숫자 여부 판별하는 함수
            strs.append(char.lower())

    print(strs)

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

print(isPalindrome_deque(input1))
print(isPalindrome_deque(input2))



