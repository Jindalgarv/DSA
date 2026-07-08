class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q=deque([(0,src,0)])
        graph=[[] for _ in range(n)]
        distance=[-1]*n

        for src,des,dis in flights:
            graph[src].append((des,dis))

        while q:
            stops,node,dis=q.popleft()
            if stops>k:
                continue
            
            for neighbour,pathlen in graph[node]:
                if distance[neighbour]==-1 or dis+pathlen<distance[neighbour]:
                    distance[neighbour]=dis+pathlen
                    q.append((stops+1,neighbour,dis+pathlen))
        return distance[dst]


