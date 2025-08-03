import unittest
import networkx as nx
from src.algoritmos.fluxo_maximo import edmonds_karp, dinic

class TestFluxoMaximo(unittest.TestCase):

    def setUp(self):
        self.G = nx.DiGraph()
        self.G.add_edge('A', 'B', capacity=10)
        self.G.add_edge('B', 'C', capacity=5)
        self.G.add_edge('A', 'C', capacity=15)

    def test_edmonds_karp(self):
        fluxo_maximo = edmonds_karp(self.G, 'A', 'C')
        self.assertEqual(fluxo_maximo, 15)

    def test_dinic(self):
        fluxo_maximo = dinic(self.G, 'A', 'C')
        self.assertEqual(fluxo_maximo, 15)

if __name__ == '__main__':
    unittest.main()