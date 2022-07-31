# 220731
# Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/

'''
1. from collections import deque
2. 스택과 큐의 특성
'''

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# 핵심: 큐로 스택을 구현해야 함!
# You must use only standard operations of a queue,
# which means that only push to back, peek/pop from front, size and is empty operations are valid.

class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        # Just use a queue where you "push to front" by pushing to back and then rotating the queue
        # until the new element is at the front (i.e., size-1 times move the front element to the back).
        self.q.append(x)    # ex) q = [1, 2]

        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft()) # # ex) q = [2, 1]
        # self.q.rotate(1)  # 위 for문을 deque의 rotate 메소드로 구현

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not len(self.q)


'''
# 나의 오답 풀이
# 테스트 케이스는 통과하지만, 제약조건을 어기는 코드
class MyStack:

    def __init__(self):
        self.q = list()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        if self.q:
            return False
        else:
            return True
'''