from Model.despesa import Despesa
from View.tela_receita import TelaRceita
from controlador_sistema import ControladorSistema
from controlador_carteira import ControladorCarteira


class ControladorReceita:
    def __init__(self):
        self.__controlador_sistema = ControladorSistema
        self.__tela_receita = TelaRceita()
        self.__controlador_carteira = ControladorCarteira()

    def opcoes_receita(self):
        while True:
            x = self.__tela_receita.tela_opcoes()
            if x == 1:
                self.inclui_receita()
            elif x == 2:
                self.lista_receita()
            elif x == 0:
                return

    def inclui_receita(self):
        carteira = self.__controlador_carteira.pega_carteira()
        dados_receita = self.__tela_receita.pega_dados_receita()
        receita = Despesa(dados_receita['carteira'], ['valor'], ['descricao'], ['categoria'], ['codigo'])
        carteira.receitas.append(receita)

    def lista_receita(self):
        carteira = self.__controlador_carteira.pega_carteira()
        if len(carteira.despesas) == 0:
            self.__tela_receita.mostra_mensagem('Lista vazia')
        else:
            for i in carteira.despesas:
                self.__tela_receita.mostra_mensagem(i.descricao + i.codigo)

    def total_receitas(self):
        carteira = self.__controlador_carteira.pega_carteira()
        total = 0
        for i in carteira.receitas:
            total += i.valor
        self.__tela_receita.mostra_mensagem(total)
