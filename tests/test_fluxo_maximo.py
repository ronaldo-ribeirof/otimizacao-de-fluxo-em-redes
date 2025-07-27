import unittest
from src.algoritmos.fluxo_maximo import edmonds_karp, dinic
from src.modelos.rede import Rede

class TestFluxoMaximo(unittest.TestCase):

    def setUp(self):
        # Configuração inicial da rede para os testes
        self.rede = Rede()
        self.rede.adicionar_no('A')
        self.rede.adicionar_no('B')
        self.rede.adicionar_no('C')
        self.rede.adicionar_arco('A', 'B', 10)
        self.rede.adicionar_arco('B', 'C', 5)
        self.rede.adicionar_arco('A', 'C', 15)

    def test_edmonds_karp(self):
        fluxo_maximo = edmonds_karp(self.rede, 'A', 'C')
        self.assertEqual(fluxo_maximo, 10)

    def test_dinic(self):
        fluxo_maximo = dinic(self.rede, 'A', 'C')
        self.assertEqual(fluxo_maximo, 10)

if __name__ == '__main__':
    unittest.main()