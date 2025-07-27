class No:
    def __init__(self, id):
        self.id = id
        self.arcos = {}

    def adicionar_arco(self, arco, capacidade):
        self.arcos[arco] = capacidade


class Rede:
    def __init__(self):
        self.nos = {}

    def adicionar_no(self, id):
        if id not in self.nos:
            self.nos[id] = No(id)

    def adicionar_arco(self, id_origem, id_destino, capacidade):
        if id_origem not in self.nos:
            self.adicionar_no(id_origem)
        if id_destino not in self.nos:
            self.adicionar_no(id_destino)
        self.nos[id_origem].adicionar_arco(id_destino, capacidade)

    def obter_capacidades(self):
        capacidades = {}
        for no in self.nos.values():
            capacidades[no.id] = no.arcos
        return capacidades

    def __str__(self):
        return f'Rede com nós: {list(self.nos.keys())}'