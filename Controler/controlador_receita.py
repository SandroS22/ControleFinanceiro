from Model.despesa import Despesa
from View.tela_receita import TelaRceita


class ControladorReceita:
    def __init__(self, controlador_sistema):
        self.__receitas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_receita = TelaRceita()

    def inclui_receita(self):
        dados_receita = self.__tela_receita.pega_dados_receita()
        receita = Despesa(dados_receita['carteira'], ['valor'], ['descricao'], ['categoria'], ['codigo'])
        return receita

    def lista_receitas(self):
        if len(self.__receitas) == 0:
            self.__tela_receita.mostra_mensagem('Lista vazia')
        else:
            for receita in self.__receitas:
                self.__tela_receita.mostra_receita(receita.codigo)

    def total_receita(self):
        total = 0
        for receita in self.__receitas:
            total += receita.valor
        return total
