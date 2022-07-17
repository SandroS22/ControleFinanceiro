from Model.despesa import Despesa
from View.tela_despesa import TelaDespesa


class ControladorDespesa:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_despesa = TelaDespesa()

    def opcoes_despesa(self):
        while True:
            op = self.__tela_despesa.tela_opcoes()
            if op == 1:
                self.inclui_despesa()
            elif op == 2:
                self.lista_despesa()
            elif op == 3:
                self.total_despesa()
            elif op == 0:
                break

    def inclui_despesa(self):
        carteira = self.__controlador_sistema.controlador_carteira.pega_carteira()
        dados_depesa = self.__tela_despesa.pega_dados_despesa()
        despesa = Despesa(dados_depesa['carteira'], dados_depesa['valor'],
                          dados_depesa['descricao'], dados_depesa['categoria'],
                          dados_depesa['codigo'])
        carteira.despesas.append(despesa)

    def lista_despesa(self):
        carteira = self.__controlador_sistema.controlador_carteira.pega_carteira()
        if len(carteira.despesas) == 0:
            self.__tela_despesa.mostra_mensagem('Lista vazia')
        else:
            for i in carteira.despesas:
                self.__tela_despesa.mostra_mensagem(i.descricao + ' ' + str(i.codigo))

    def total_despesa(self):
        carteira = self.__controlador_sistema.controlador_carteira.pega_carteira()
        total = 0
        for i in carteira.despesas:
            total += i.valor
        self.__tela_despesa.mostra_mensagem(total)
