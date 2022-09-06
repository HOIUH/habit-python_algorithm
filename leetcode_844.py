# 220906
# Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/

'''
1. List를 Stack처럼 사용
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        # 별도 함수로 뽑아낸 코드
        def build(S):
            ans = []
            for e in S:
                if e != '#':
                    ans.append(e)
                elif ans:   # ans가 비어있지 않은 경우에만 pop
                    ans.pop()
            return ans
            # return ''.join(ans)   # 더 오래 걸림

        return build(s) == build(t)

# 나의 풀이
'''
        s_temp, t_temp = [], []
        for i in range(len(s)):
            if s[i] == '#':
                if s_temp:
                    s_temp.pop()
            else:
                s_temp.append(s[i])

        for i in range(len(t)):
            if t[i] == '#':
                if t_temp:
                    t_temp.pop()
            else:
                t_temp.append(t[i])

        if s_temp == t_temp:
            return True
        else:
            return False
'''