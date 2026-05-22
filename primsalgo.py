import heapq

def prims(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (weight, node)
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))
                mst_edges.append((node, neighbor, edge_weight))

    return total_cost


# Example graph (Adjacency List)
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}

print("Total MST Cost:", prims(graph, 0))
