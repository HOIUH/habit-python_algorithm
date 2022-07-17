# 220717
# Decode the Message
# https://leetcode.com/problems/decode-the-message/

'''
1. 리스트 순서 유지하고 중복 제거 (https://m31phy.tistory.com/130)
'''

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key = key.replace(' ', '')
        list_key = sorted(set(key), key= lambda x: key.index(x))
        mapping = dict(zip(list_key, list(alphabet)))

        result = ''
        for i in range(len(message)):
            if message[i] == ' ':
                result += ' '
            else:
                result += mapping[message[i]]
        return result

key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
a = Solution()
print(a.decodeMessage(key, message))