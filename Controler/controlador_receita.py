from Model.despesa import Despesa
from View.tela_receita import TelaRceita
from controlador_sistema import ControladorSistema


class ControladorReceita:
    def __init__(self):
        self.__controlador_sistema = ControladorSistema
        self.__tela_receita = TelaRceita()

    def inclui_receita(self, carteira):
        dados_receita = self.__tela_receita.pega_dados_receita()
        receita = Despesa(dados_receita['carteira'], ['valor'], ['descricao'], ['categoria'], ['codigo'])
        carteira.receitas.append(receita)

    def lista_receita(self, carteira):
        if len(carteira.despesas) == 0:
            self.__tela_receita.mostra_mensagem('Lista vazia')
        else:
            for i in carteira.despesas:
                self.__tela_receita.mostra_mensagem(i.descricao + i.codigo)

    def total_receitas(self, carteira):
        total = 0
        for i in carteira.receitas:
            total += i.valor
        self.__tela_receita.mostra_mensagem(total)
