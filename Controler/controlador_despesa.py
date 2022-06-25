from Model.despesa import Despesa
from View.tela_despesa import TelaDespesa


class ControladorDespesa:
    def __init__(self, controlador_sistema):
        self.__despesas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_despesa = TelaDespesa()

    def inclui_despesa(self):
        dados_depesa = self.__tela_despesa.pega_dados_despesa()
        despesa = Despesa(dados_depesa['carteira'], ['valor'], ['descricao'], ['categoria'], ['codigo'])
        return despesa

    def lista_despesa(self):
        if len(self.__despesas) == 0:
            self.__tela_despesa.mostra_mensagem('Lista vazia')
        else:
            for despesa in self.__despesas:
                self.__tela_despesa.mostra_despesa(despesa.codigo)

    def total_despesa(self):
        total = 0
        for despesa in self.__despesas:
            total += despesa.valor
        return total
