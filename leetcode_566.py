# 220604
# Reshape the Matrix
# https://leetcode.com/problems/reshape-the-matrix/

def list_chuck(self, arr: List, n: int) -> List:
    return [arr[i: i + n] for i in range(0, len(arr), n)]


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        output = []
        if (m * n) % (r * c) == 0:
            x = int(c / n)
            if x >= 1:
                for i in range(0, len(mat) - x + 1, x):
                    output.append(sum(mat[i:i + x], []))
            else:
                for i in range(0, len(mat)):
                    output.append(list_chunk(mat[i], c))
            return output
        else:
            return mat


