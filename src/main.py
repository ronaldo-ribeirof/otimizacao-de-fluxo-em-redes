import networkx as nx

def main():
    # Criação do grafo dirigido
    G = nx.DiGraph()
    # Adicionando nós e arcos com capacidade
    G.add_edge('A', 'B', capacity=10)
    G.add_edge('A', 'C', capacity=5)
    G.add_edge('B', 'C', capacity=15)

    origem = 'A'
    destino = 'C'

    # Edmonds-Karp (default)
    fluxo_ek = edmonds_karp(G, origem, destino)
    print(f"Fluxo máximo (Edmonds-Karp): {fluxo_ek}")

    # Dinic
    fluxo_dinic = dinic(G, origem, destino)
    print(f"Fluxo máximo (Dinic): {fluxo_dinic}")

if __name__ == "__main__":
    main()