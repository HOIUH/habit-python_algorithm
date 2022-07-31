# 220731
# Sorting the Sentence
# https://leetcode.com/problems/sorting-the-sentence/

'''
1. List into String => '구분자'.join(리스트)
2. List.sort(key=lambda x: x[-1])
'''

class Solution:

    # 나의 풀이
    def sortSentence(self, s: str) -> str:
        split_s = s.split(' ')
        answer = [''] * 9
        # answer = [None] * len(split_s)

        for ss in split_s:
            idx = int(ss[-1]) - 1
            answer[idx] = ss[:-1]

        return ' '.join(answer).strip()     # answer의 length를 9로 명시했기 때문에 strip() 필요

    # sort를 사용한 다른 사람 풀이
    '''
    def sortSentence(self, s: str) -> str:
        sentence = s.split(" ")
        sentence.sort(key=lambda x: x[-1])
        
        return " ".join(word[:-1] for word in sentence)
    '''

'''
s = "is2 sentence4 This1 a3"
a = Solution()
print(a.sortSentence(s))
'''