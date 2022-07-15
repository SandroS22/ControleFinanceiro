from Model.abstract_movimentacao import Movimentacao


class Despesa(Movimentacao):
    def __init__(self, carteira, valor, descricao, categoria, codigo):
        super().__init__(carteira, valor, descricao, categoria, codigo)
        self.valor = valor - (valor * 2)
