# 220710
# Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # replace 사용
        # 나의 풀이
        # return address.replace('.', '[.]')

        # join 과 split 사용
        # return '[.]'.join(address.split('.'))

        # re.sub 사용
        # 가장 짧은 runtime
        # return re.sub('\.', '[.]', address)

        # inline 조건문과 join 사용
        return ''.join('[.]' if c == '.' else c for c in address)