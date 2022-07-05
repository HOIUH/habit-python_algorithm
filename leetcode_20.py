# 220705
# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

'''
1. List as Stack
2. Dictionary
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', ']': '[', '}': '{'}

        for element in s:
            if element in brackets.values():  # Opening Bracket
                stack.append(element)
            else:  # Closing Bracket
                if stack and brackets[element] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False

        # 나의 오답
        '''
        for element in s:
            stack.append(element)

            if element == ')':
                if stack[-2] != '(':
                    return False
                else:
                    stack.pop()
                    stack.pop()
            elif element == ']':
                if stack[-2] != '[':
                    return False
                else:
                    stack.pop()
                    stack.pop()
            elif element == '}':
                if stack[-2] != '{':
                    return False
                else:
                    stack.pop()
                    stack.pop()
        '''