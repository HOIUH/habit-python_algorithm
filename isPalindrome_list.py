input1 = "A man, a plan, a canal: Panama"
input2 = "race a car"

# 리스트로 변환
def isPalindrome(s:str) -> bool:
    strs = []
    
    for char in s:
        if char.isalnum():	# 영문자, 숫자 여부 판별하는 함수
            strs.append(char.lower())
    
    print(strs)        
            
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():	# 파이썬 리스트는 pop() 함수에서 인덱스 지정 가능
            return False
        
    return True
    
print(isPalindrome(input1))
print(isPalindrome(input2))



