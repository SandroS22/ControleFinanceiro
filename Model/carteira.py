class Carteira:
    def __init__(self, nome, codigo):
        self.__nome = nome
        self.__codigo = codigo
        self.__receitas = []
        self.__despesas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def codigo(self):
        return self.__codigo

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def receitas(self):
        return self.__receitas

    @property
    def despesas(self):
        return self.__despesas
