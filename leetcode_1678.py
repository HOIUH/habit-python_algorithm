# 220823
# Goal Parser Interpretation
# https://leetcode.com/problems/goal-parser-interpretation/

'''
1. re.sub
2. 정규표현식: https://wikidocs.net/4308
3. Method Chaining: 메소드가 객체를 반환하게 되면, 메소드의 반환 값이 객체를 통해 또 다른 함수를 호출
'''

import re

class Solution:
    def interpret(self, command: str) -> str:

        # 풀이 1. re.sub과 정규표현식 사용
        return re.sub('\(al\)', 'al', re.sub('\(\)', 'o', command))

        # 풀이 2. replace 함수 사용
        '''
        command = command.replace('()', 'o')
        command = command.replace('(al)', 'al')
        return command
        '''
        # 위 주석처리된 코드를 한줄로
        return command.replace('()', 'o').replace('(al)', 'al')     # 메소드 체이닝