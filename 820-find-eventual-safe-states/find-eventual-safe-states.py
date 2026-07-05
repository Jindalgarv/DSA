class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n
        # 0 = unvisited
        # 1 = currently in DFS path / unsafe
        # 2 = confirmed safe

        def isSafe(node):
            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1

            for neighbour in graph[node]:
                if not isSafe(neighbour):
                    return False

            state[node] = 2
            return True

        return [node for node in range(n) if isSafe(node)]