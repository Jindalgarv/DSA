    #just check topological sort and return it 
    #use kahn's algorithm
class Solution:
    def findOrder(
        self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        order = []

        # To take course u, course v must be completed first:
        # v -> u
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbour in graph[node]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return order if len(order) == numCourses else []