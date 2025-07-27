def main():
    # Inicializa a rede de telecomunicações
    from modelos.rede import Rede
    from algoritmos.fluxo_maximo import edmonds_karp, dinic

    # Criação da rede
    rede = Rede()

    # Adicionando nós e arcos à rede
    rede.adicionar_no('A')
    rede.adicionar_no('B')
    rede.adicionar_no('C')
    rede.adicionar_arco('A', 'B', 10)
    rede.adicionar_arco('A', 'C', 5)
    rede.adicionar_arco('B', 'C', 15)

    # Definindo os nós de origem e destino
    origem = 'A'
    destino = 'C'

    # Calculando o fluxo máximo usando o algoritmo de Edmonds-Karp
    fluxo_maximo_ek = edmonds_karp(rede, origem, destino)
    print(f"Fluxo máximo (Edmonds-Karp): {fluxo_maximo_ek}")

    # Calculando o fluxo máximo usando o algoritmo de Dinic
    fluxo_maximo_dinic = dinic(rede, origem, destino)
    print(f"Fluxo máximo (Dinic): {fluxo_maximo_dinic}")

if __name__ == "__main__":
    main()