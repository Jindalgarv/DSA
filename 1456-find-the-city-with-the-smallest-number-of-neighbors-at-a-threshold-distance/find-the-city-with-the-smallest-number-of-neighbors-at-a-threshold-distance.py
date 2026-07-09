class Solution:
    def findTheCity(
        self,
        n: int,
        edges: List[List[int]],
        distanceThreshold: int
    ) -> int:
        
        dist = [[float('inf')] * n for _ in range(n)]

        for city in range(n):
            dist[city][city] = 0

        for u, v, weight in edges:
            dist[u][v] = weight
            dist[v][u] = weight

        # Floyd-Warshall
        for via in range(n):
            for src in range(n):
                for dst in range(n):
                    dist[src][dst] = min(
                        dist[src][dst],
                        dist[src][via] + dist[via][dst]
                    )

        min_reachable = n
        answer = -1

        for city in range(n):
            reachable = 0

            for neighbor in range(n):
                if (
                    city != neighbor
                    and dist[city][neighbor] <= distanceThreshold
                ):
                    reachable += 1

            # <= ensures larger city index wins in a tie
            if reachable <= min_reachable:
                min_reachable = reachable
                answer = city

        return answer