class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        q1,q2=deque(s),deque(goal)
        for i in range(len(q1)):
            q1.appendleft(q1.pop())
            if q1==q2:
                return True
        return False

        