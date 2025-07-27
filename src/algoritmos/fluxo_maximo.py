class Rede:
    def __init__(self):
        self.grafo = {}
    
    def adicionar_arco(self, origem, destino, capacidade):
        if origem not in self.grafo:
            self.grafo[origem] = {}
        self.grafo[origem][destino] = capacidade

def edmonds_karp(rede, fonte, sorvedouro):
    fila = []
    pais = {}
    fluxo_maximo = 0

    while True:
        fila.append(fonte)
        pais = {fonte: None}
        while fila:
            u = fila.pop(0)
            for v in rede.grafo.get(u, {}):
                if v not in pais and rede.grafo[u][v] > 0:
                    pais[v] = u
                    if v == sorvedouro:
                        break
                    fila.append(v)
            if sorvedouro in pais:
                break
        else:
            break

        fluxo = float('Inf')
        v = sorvedouro
        while v != fonte:
            u = pais[v]
            fluxo = min(fluxo, rede.grafo[u][v])
            v = u

        v = sorvedouro
        while v != fonte:
            u = pais[v]
            rede.grafo[u][v] -= fluxo
            if v not in rede.grafo:
                rede.grafo[v] = {}
            if u not in rede.grafo[v]:
                rede.grafo[v][u] = 0
            rede.grafo[v][u] += fluxo
            v = u

        fluxo_maximo += fluxo

    return fluxo_maximo

def dinic(rede, fonte, sorvedouro):
    # Implementação do algoritmo de Dinic
    pass

def calcular_fluxo_maximo(rede, fonte, sorvedouro, algoritmo='edmonds_karp'):
    if algoritmo == 'edmonds_karp':
        return edmonds_karp(rede, fonte, sorvedouro)
    elif algoritmo == 'dinic':
        return dinic(rede, fonte, sorvedouro)
    else:
        raise ValueError("Algoritmo desconhecido: {}".format(algoritmo))