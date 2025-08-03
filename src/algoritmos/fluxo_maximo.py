import networkx as nx
from collections import deque

def edmonds_karp(G, fonte, sorvedouro):
    fluxo, _ = nx.maximum_flow(G, fonte, sorvedouro, flow_func=nx.algorithms.flow.edmonds_karp)
    return fluxo

def dinic(G, fonte, sorvedouro):
    residual = nx.DiGraph()
    for u, v, data in G.edges(data=True):
        capacidade = data.get('capacity', 0)
        if capacidade > 0:
            residual.add_edge(u, v, capacity=capacidade)
            if not residual.has_edge(v, u):
                residual.add_edge(v, u, capacity=0)

    def bfs_level():
        level = {node: -1 for node in residual.nodes}
        queue = deque([fonte])
        level[fonte] = 0
        while queue:
            u = queue.popleft()
            for v in residual.successors(u):
                if residual[u][v]['capacity'] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level

    def dfs(u, fluxo, level, next_arc):
        if u == sorvedouro:
            return fluxo
        total_sent = 0
        neighbors = list(residual.successors(u))
        while next_arc[u] < len(neighbors):
            v = neighbors[next_arc[u]]
            if residual[u][v]['capacity'] > 0 and level[v] == level[u] + 1:
                sent = dfs(v, min(fluxo, residual[u][v]['capacity']), level, next_arc)
                if sent > 0:
                    residual[u][v]['capacity'] -= sent
                    residual[v][u]['capacity'] += sent
                    total_sent += sent
                    fluxo -= sent
                    if fluxo == 0:
                        break
            next_arc[u] += 1
        return total_sent

    fluxo_maximo = 0
    while True:
        level = bfs_level()
        if level[sorvedouro] < 0:
            break
        next_arc = {node: 0 for node in residual.nodes}
        while True:
            sent = dfs(fonte, float('inf'), level, next_arc)
            if sent == 0:
                break
            fluxo_maximo += sent
    return fluxo_maximo