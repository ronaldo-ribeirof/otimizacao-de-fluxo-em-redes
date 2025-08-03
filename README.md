# Projeto de Otimização de Fluxo Máximo em Redes de Telecomunicações

Este projeto implementa uma solução para o problema de fluxo máximo em redes de telecomunicações. Utilizando algoritmos como Edmonds-Karp e Dinic, o objetivo é calcular a capacidade máxima de tráfego de dados em uma rede representada como um grafo.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
otimizacao-fluxo-maximo
├── src
│   ├── main.py                # Ponto de entrada da aplicação
│   ├── algoritmos
│   │   └── fluxo_maximo.py    # Implementação dos algoritmos de fluxo máximo
│   ├── modelos
│   │   └── rede.py            # Definição da estrutura da rede de telecomunicações
│   └── utils
│       └── helpers.py         # Funções auxiliares para manipulação de dados
├── tests
│   └── test_fluxo_maximo.py   # Testes automatizados para os algoritmos
├── requirements.txt            # Dependências do projeto
└── README.md                   # Documentação do projeto
```

## Como Executar

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd otimizacao-fluxo-maximo
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Execute o programa:
   ```
   python src/main.py
   ```

## Exemplos de Uso

Após a execução do programa, você poderá visualizar a capacidade máxima de tráfego de dados calculada para a rede configurada. O arquivo `main.py` contém exemplos de como inicializar a rede e executar os algoritmos.

## Dependências

As bibliotecas necessárias para a execução do projeto estão listadas no arquivo `requirements.txt`. Certifique-se de que todas as dependências estejam instaladas antes de executar o código.
