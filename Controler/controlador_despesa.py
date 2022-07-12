from Model.despesa import Despesa
from View.tela_despesa import TelaDespesa
from controlador_sistema import ControladorSistema


class ControladorDespesa:
    def __init__(self):
        self.__controlador_sistema = ControladorSistema()
        self.__tela_despesa = TelaDespesa()

    def inclui_despesa(self, carteira):
        dados_depesa = self.__tela_despesa.pega_dados_despesa()
        despesa = Despesa(dados_depesa['carteira'], ['valor'], ['descricao'], ['categoria'], ['codigo'])
        carteira.despesas.append(despesa)

    def lista_despesa(self, carteira):
        if len(carteira.despesas) == 0:
            self.__tela_despesa.mostra_mensagem('Lista vazia')
        else:
            for i in carteira.despesas:
                self.__tela_despesa.mostra_mensagem(i.descricao + i.codigo)

    def total_despesa(self, carteira):
        total = 0
        for i in carteira.despesas:
            total += i.valor
        self.__tela_despesa.mostra_mensagem(total)
