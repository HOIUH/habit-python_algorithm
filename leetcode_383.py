# 220610
# Ransom Note
# https://leetcode.com/problems/ransom-note/

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        for r in ransomNote:
            if r in magazine:
                magazine = magazine.replace(r, '', 1)
            else:
                return False

        return True









