class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        time = [float('inf')] * (n + 1)
        time[k] = 0

        pq = [(0, k)]

        while pq:
            t, node = heappop(pq)

            if t > time[node]:
                continue

            for neighbour, weight in graph[node]:
                new_time = t + weight

                if new_time < time[neighbour]:
                    time[neighbour] = new_time
                    heappush(pq, (new_time, neighbour))

        ans = max(time[1:])
        return -1 if ans == float('inf') else ans