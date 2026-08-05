class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
#NOT OPTIMAL BECAUSE COMPARING Q1 AND Q2 ALSO TAKES O(N) SO OVERALL IT IS N SQ

        # if s==goal:
        #     return True
        # q1,q2=deque(s),deque(goal)
        # for i in range(len(q1)):
        #     q1.appendleft(q1.pop())
        #     if q1==q2:
        #         return True
        # return False

        return len(s) == len(goal) and goal in (s + s)

        