def has_circular_dependency(n, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)

    visit = [False] * n
    on_path = [False] * n

    def dfs(node):
        visit[node] = True
        on_path[node] = True

        for neighbor in graph[node]:
            if not visit[neighbor]:
                if dfs(neighbor):
                    return True
            elif on_path[neighbor]:
                return True

        on_path[node] = False
        return False

    for i in range(n):
        if not visit[i]:
            if dfs(i):
                return True

    return False

if __name__ == "__main__":
    n1 = 4
    edges1 = [[0, 1], [1, 2], [2, 3]]
    print("Example 1:", has_circular_dependency(n1, edges1))

    n2 = 4
    edges2 = [[0, 1], [1, 2], [2, 0]]
    print("Example 2:", has_circular_dependency(n2, edges2))
