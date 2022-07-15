from abc import ABC
from Model.categoria import Categoria
from Model.carteira import Carteira


class Movimentacao(ABC):
    def __int__(self, carteira, valor, descricao, categoria, codigo):
        self.__valor = valor
        self.__descricao = descricao
        self.__categoria = categoria
        self.__codigo = codigo
        self.__carteira = carteira

    @property
    def valor(self):
        return self.__valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def categoria(self):
        return self.__categoria

    @property
    def codigo(self):
        return self.__codigo

    @property
    def carteira(self):
        return self.__carteira

    @valor.setter
    def valor(self, valor):
        if isinstance(valor, float):
            self.__valor = valor

    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @categoria.setter
    def categoria(self, categoria):
        if isinstance(categoria, Categoria):
            self.__categoria = categoria

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @carteira.setter
    def carteira(self, carteira):
        if isinstance(carteira, Carteira):
            self.__carteira = carteira
