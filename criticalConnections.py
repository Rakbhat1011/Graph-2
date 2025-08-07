"""
Perform DFS and assign discovery time and lowest reachable time for each node
If low[neighbor] > disc[current], then the edge (current, neighbor) is a bridge
Use Tarjan’s bridge-finding algorithm to efficiently track and return such edges
"""
"""
Time Complexity: O(V + E)	DFS traversal
Space Complexity: O(V + E)	Graph + disc/low arrays
"""


class criticalConnections:
    def criticalConnection(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n
        low = [-1] * n
        time = 0
        res = []

        def dfs(u, parent):
            nonlocal time
            disc[u] = low[u] = time
            time += 1

            for v in graph[u]:
                if v == parent:
                    continue
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        res.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])

        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)

        return res


if __name__ == "__main__":
    sol = criticalConnections()
    print(sol.criticalConnection(4, [[0,1],[1,2],[2,0],[1,3]]))  # [[1,3]]
    print(sol.criticalConnection(2, [[0,1]]))                   # [[0,1]]
    print(sol.criticalConnection(5, [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]))  # []


