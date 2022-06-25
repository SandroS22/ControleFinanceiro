from abstract_movimentacao import Movimentacao


class Receita(Movimentacao):
    def __init__(self, carteira, valor, descricao, categoria, codigo):
        super().__init__(carteira, valor, descricao, categoria, codigo)
